from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
from  utils.validation import validate_contact
from database import SessionLocal

class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String,nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    
    #ADD CONTACT
    @classmethod
    def add_contact(cls, name, phone_number, email):
            db = SessionLocal()

            try:
                validate_contact(name, phone_number, email)
                new_contact = cls(
                    name=name,
                    phone_number=phone_number,
                    email=email
                )

                db.add(new_contact)
                db.commit()
                db.refresh(new_contact)

                print("Contact saved successfully")
                return new_contact

            except Exception as e:
                db.rollback()
                print("Error:", e)
                

            finally:
                db.close()
                
               
     #DELETE CONTACT
    @classmethod
    def delete_contact(cls):

        db = SessionLocal()

        try:

            print("\nDelete Contact By:")
            print("1. Contact ID")
            print("2. Name")
            print("3. Phone Number")
            print("4. Email")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                contact_id = int(input("Enter Contact ID: "))

                contact = db.query(cls).filter(
                    cls.contact_id == contact_id
                ).first()

            elif choice == 2:

                name = input("Enter Name: ")

                contact = db.query(cls).filter(
                    cls.name.ilike(name)
                ).first()

            elif choice == 3:

                phone_number = input("Enter Phone Number: ")

                contact = db.query(cls).filter(
                    cls.phone_number == phone_number
                ).first()

            elif choice == 4:

                email = input("Enter Email: ")

                contact = db.query(cls).filter(
                    cls.email == email
                ).first()

            else:

                print("Invalid Choice")
                return None

            if not contact:

                print("Contact not found")
                return None

            print("\nContact Found")
            print(f"ID    : {contact.contact_id}")
            print(f"Name  : {contact.name}")
            print(f"Phone : {contact.phone_number}")
            print(f"Email : {contact.email}")

            confirm = input(
                "\nAre you sure you want to delete this contact? (y/n): "
            )

            if confirm.lower() != "y":

                print("Deletion cancelled")
                return None

            db.delete(contact)
            db.commit()

            print("Contact deleted successfully")

        except Exception as e:

            db.rollback()
            print("Error:", e)

        finally:

            db.close()
   
   #DISPLAY CONTACT
    @classmethod
    def display_contact(cls):

        db = SessionLocal()

        try:

            print("\n1. Display Particular Contact")
            print("2. Display All Contacts")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                print("\nDisplay Contact By:")
                print("1. Contact ID")
                print("2. Name")
                print("3. Email")

                search_choice = int(input("Enter your choice: "))

                if search_choice == 1:

                    contact_id = int(input("Enter Contact ID: "))

                    contacts = db.query(cls).filter(
                        cls.contact_id == contact_id
                    ).all()

                elif search_choice == 2:

                    name = input("Enter Name: ")

                    contacts = db.query(cls).filter(
                        cls.name.ilike(f"%{name}%")
                    ).all()

                elif search_choice == 3:

                    email = input("Enter Email: ")

                    contacts = db.query(cls).filter(
                        cls.email == email
                    ).all()

                else:

                    print("Invalid Choice")
                    return

            elif choice == 2:

                contacts = db.query(cls).all()

            else:

                print("Invalid Choice")
                return

            if not contacts:

                print("No contacts found")
                return

            print("-" * 80)
            print(f"{'ID':<5} {'NAME':<20} {'PHONE':<15} {'EMAIL'}")
            print("-" * 80)

            for contact in contacts:

                print(
                    f"{contact.contact_id:<5} "
                    f"{contact.name:<20} "
                    f"{contact.phone_number:<15} "
                    f"{contact.email}"
                )

            print("-" * 80)

        except Exception as e:

            print("Error:", e)

        finally:

            db.close()
            
            
    #UPDATE CONTACT
    @classmethod
    def update_contact(cls):

        db = SessionLocal()

        try:
            
            print("\nUpdate Contact By:")
            print("1. Contact ID")
            print("2. Name")
            print("3. Email")

            choice = int(input("Enter your choice: "))

            contact = None

            if choice == 1:
                contact_id = int(input("Enter Contact ID: "))
                contact = db.query(cls).filter(
                    cls.contact_id == contact_id
                ).first()

            elif choice == 2:
                name = input("Enter Name: ")
                contacts = db.query(cls).filter(
                    cls.name.ilike(f"%{name}%")
                ).all()

                if not contacts:
                    print("No contacts found!")
                    return

                print("\nMatching Contacts:")
                for c in contacts:
                    print(
                        f"ID: {c.contact_id}, "
                        f"Name: {c.name}, "
                        f"Phone: {c.phone_number}, "
                        f"Email: {c.email}"
                    )

                contact_id = int(
                    input("\nEnter Contact ID to update: ")
                )

                contact = db.query(cls).filter(
                    cls.contact_id == contact_id
                ).first()

            elif choice == 3:
                email = input("Enter Email: ")

                contact = db.query(cls).filter(
                    cls.email == email
                ).first()

            else:
                print("Invalid choice!")
                return

            if not contact:
                print("Contact not found!")
                return

            print("\nCurrent Details:")
            print(f"Name  : {contact.name}")
            print(f"Phone : {contact.phone_number}")
            print(f"Email : {contact.email}")
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")

            update_choice = int(input("Enter your choice: "))
        
            new_name = contact.name
            new_phone = contact.phone_number
            new_email = contact.email

            if update_choice == 1:

                new_name = input("Enter New Name: ")

            elif update_choice == 2:

                new_phone = input("Enter New Phone: ")

            elif update_choice == 3:

                new_email = input("Enter New Email: ")

            else:

                print("Invalid Choice!")
                return

            validate_contact(
                new_name,
                new_phone,
                new_email
            )

            contact.name = new_name
            contact.phone_number = new_phone
            contact.email = new_email

            db.commit()
            db.refresh(contact)

            print("Contact updated successfully!")

        except Exception as e:

            db.rollback()
            print("Error:", e)

        finally:

            db.close()
      
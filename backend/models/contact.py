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
                
     #           
    @classmethod
    def update_contact(cls, contact_id):

        db = SessionLocal()

        try:

            # validate_contact(name, phone_number, email)

            contact = db.query(cls).filter(
                cls.contact_id == contact_id
            ).first()

            if not contact:
                print("Contact not found")
                return None
            print(contact.name)
            print("What do u want to update?")
            print("1.Name")
            print("2.Phone number")
            print("3.Email")
            choice=int(input("Enter your choice:"))
            if choice==1:
                name =  input("Enter the name:")
                contact.name = name
            if choice==2:
                phone_number =  input("Enter the Phone Number:")
                contact.phone_number = phone_number
            if choice==3:
                email =  input("Enter the Email:")
                contact.email = email
    
            db.commit()
            db.refresh(contact)

            print("Contact updated successfully")
            return contact

        except Exception as e:

            db.rollback()
            print("Error:", e)

        finally:

            db.close()
            
       
    
     # delete_contact
    @classmethod
    def delete_contact(cls, contact_id):

        db = SessionLocal()

        try:

            contact = db.query(cls).filter(
                cls.contact_id == contact_id
            ).first()

            if not contact:
                print("Contact not found")
                return None

            print(f"Contact Found: {contact.name}")

            confirm = input("Are you sure you want to delete this contact? (y/n): ")

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
    # def display_contact(cls):

    #     db = SessionLocal()

    #     try:

    #         print("1. Display Particular Contact")
    #         print("2. Display All Contacts")

    #         choice = int(input("Enter your choice: "))

    #         if choice == 1:

    #             contact_id = int(input("Enter Contact ID: "))

    #             contact = db.query(cls).filter(
    #                 cls.contact_id == contact_id
    #             ).first()

    #             if not contact:
    #                 print("Contact not found")
    #                 return

    #             print(f"ID    : {contact.contact_id}")
    #             print(f"Name  : {contact.name}")
    #             print(f"Phone : {contact.phone_number}")
    #             print(f"Email : {contact.email}")

    #         elif choice == 2:

    #             contacts = db.query(cls).all()

    #             if not contacts:
    #                 print("No contacts found")
    #                 return

    #             for contact in contacts:
    #                 print("-" * 30)
    #                 print(f"ID    : {contact.contact_id}")
    #                 print(f"Name  : {contact.name}")
    #                 print(f"Phone : {contact.phone_number}")
    #                 print(f"Email : {contact.email}")

    #         else:
    #             print("Invalid Choice")

    #     except Exception as e:
    #         print("Error:", e)

    #     finally:
    #          db.close()
    @classmethod
   
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
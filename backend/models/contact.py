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
   
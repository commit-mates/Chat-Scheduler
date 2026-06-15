from models.contact import Contact
from  utils.validation import validate_contact
from database import Base ,engine
from models.message import ScheduledMessage
from models.scheduler import NotificationLog, SchedulerLog


Base.metadata.create_all(bind=engine)

# name = input("Enter Name: ")
# phone = input("Enter Phone Number: ")
# email = input("Enter Email: ")


#Contact.add_contact(name, phone, email)
contact_id = int(input("Enter Contact Id:"))
Contact.update_contact(contact_id)



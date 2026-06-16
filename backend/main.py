from models.contact import Contact
from  utils.validation import validate_contact
from database import Base ,engine
from models.message import ScheduledMessage
from models.scheduler import NotificationLog, SchedulerLog


Base.metadata.create_all(bind=engine)

# from models.contact import Contact
from database import Base, engine

Base.metadata.create_all(bind=engine)

while True:

    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        Contact.add_contact(name, phone, email)

    elif choice == 2:

        contact_id = int(input("Enter Contact ID: "))
        Contact.update_contact(contact_id)

    elif choice == 3:

        contact_id = int(input("Enter Contact ID: "))
        Contact.delete_contact(contact_id)

    elif choice == 4:

        Contact.display_contact()

    elif choice == 5:

        print("Thank you!")
        break

    else:

        print("Invalid Choice")
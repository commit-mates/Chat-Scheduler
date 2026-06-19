from models.contact import Contact
from utils.validation import validate_contact
from database import Base ,engine
from models.message import ScheduledMessage
from models.scheduler import NotificationLog, SchedulerLog

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
        Contact.add_contact()
    elif choice == 2:
         Contact.update_contact()       
    elif choice == 3:
        Contact.delete_contact()
    elif choice == 4:
        Contact.display_contact()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")
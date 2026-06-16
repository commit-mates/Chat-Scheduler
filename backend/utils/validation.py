def validate_contact(name,phone_number,email):

    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    if not phone_number:
        raise ValueError("Phone number cannot be empty")
    

    if not phone_number.isdigit():
        raise ValueError("Phone number must contain only digits")
    

    if len(phone_number) != 10:
        raise ValueError("Phone number must be 10 digits")


    if not email:
        raise ValueError("Email cannot be empty")
         

    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")
           
        
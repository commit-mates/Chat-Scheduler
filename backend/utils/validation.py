import re
def validate_contact(name,phone_number,email):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    if not phone_number:
        raise ValueError("Phone number cannot be empty")
    if not phone_number:
        raise ValueError("Phone number cannot be empty")
    phone_number = phone_number.strip()
    if not phone_number.isdigit():
         raise ValueError("Enter digits only. Do not enter alphabets.")
    if not re.fullmatch(r"\d{10}", phone_number):
     raise ValueError(
        "Phone number must be 10 digits or start with +91 followed by 10 digits")
    # if len(phone_number) != 10:
    #     raise ValueError("Phone number must be 10 digits")
    if not email:
        raise ValueError("Email cannot be empty")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")
    if not email:
      raise ValueError("Email cannot be empty")
    email = email.strip().lower()
    if email.count("@") != 1:
        raise ValueError("Email should contain exactly one @")
    username, domain = email.split("@")
    if not username:
        raise ValueError("Email cannot start with @")
    if "." not in domain:
        raise ValueError("Invalid email address")            
		
		
		
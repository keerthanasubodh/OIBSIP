import string
import random

def generate_password(length=12, use_special_chars=True):
    """
    Generate a random password of specified length.
    If use_special_chars is True, the password may contain special characters.
    """
    # Define the character sets to use for generating the password
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    special_chars = string.punctuation

    # Combine the character sets based on the use_special_chars flag
    if use_special_chars:
        all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    else:
        all_chars = lowercase_chars + uppercase_chars + number_chars

    # Generate the password by randomly selecting characters from the combined character set
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # Ensure that the password contains at least one lowercase letter, one uppercase letter, and one number
    while (not any(c.islower() for c in password) or
           not any(c.isupper() for c in password) or
           not any(c.isdigit() for c in password)):
        password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Example usage
print(generate_password())

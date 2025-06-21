import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long."

    # Combine letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to select characters
    password = ''.join(random.choices(characters, k=length))

    return password

# --- Main program starts here ---
print("🔐 Strong Password Generator 🔐")
print("-------------------------------")

try:
    user_length = int(input("Enter desired password length: "))
    generated_password = generate_password(user_length)
    print("Your new password is:")
    print(generated_password)

except ValueError:
    print("Please enter a valid number.")

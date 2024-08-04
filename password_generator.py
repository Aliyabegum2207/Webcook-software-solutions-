import random
import string
import pyperclip
from cryptography.fernet import Fernet

def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    character_set = ''
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character types selected for password generation.")
    
    return ''.join(random.choice(character_set) for _ in range(length))

def save_password(password, filename):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())

    with open(filename, 'wb') as file:
        file.write(key + b'\n' + encrypted_password)

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    try:
        password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
        print(f"Generated Password: {password}")

        copy_to_clipboard = input("Copy the password to the clipboard? (yes/no): ").strip().lower() == 'yes'
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard.")
        
        save_to_file = input("Save the password to a file securely? (yes/no): ").strip().lower() == 'yes'
        if save_to_file:
            filename = input("Enter the filename to save the password: ")
            save_password(password, filename)
            print(f"Password saved securely to {filename}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

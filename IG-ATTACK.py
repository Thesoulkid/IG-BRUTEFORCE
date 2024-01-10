from cryptography.fernet import Fernet
import os
import webbrowser

def generate_key():
    return Fernet.generate_key()

def save_key_to_file(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def load_key_from_file(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    original_file_path = encrypted_file_path[:-4]  # Remove '.enc' extension
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)

def ask_for_permission():
    user_response = input("Are you using this script for educational purposes? (yes/no): ").lower()
    return user_response == 'yes'

def check_telegram_membership():
    user_response = input("Are you a member of our Telegram group? (yes/no): ").lower()
    return user_response == 'yes'

def ask_for_key():
    user_response = input("Do you have the encryption key? (yes/no): ").lower()
    return user_response == 'yes'

if __name__ == "__main__":
    permission_given = ask_for_permission()

    if not permission_given:
        print("Sorry, this script is only for educational purposes.")
        exit()

    telegram_member = check_telegram_membership()

    if not telegram_member:
        print("Please join our Telegram group: https://t.me/WHITEDR00M")
        webbrowser.open("https://t.me/WHITEDR00M")
        exit()

    key_present = ask_for_key()

    if not key_present:
        key_file = 'encryption_key.key'  # Specify the file to store the encryption key
        encryption_key = generate_key()
        save_key_to_file(encryption_key, key_file)
    else:
        key_file = 'encryption_key.key'  # Specify the file to store the encryption key

        if os.path.exists(key_file):
            # Load the key from the file for decryption
            encryption_key = load_key_from_file(key_file)
        else:
            print("Encryption key file not found.")
            exit()

    script_path = 'reading.py'  # Replace with the actual path to your project.py file
    encrypted_script_path = 'reading.py.enc'  # Replace with the actual path to your encrypted script file

    try:
        decrypt_file(encrypted_script_path, encryption_key)
        exec(open('reading.py').read())
    except Exception as e:
        custom_error_message = "Invalid key or decryption error. Please check if the key is correct."
        print(custom_error_message)
        print(f"Original Exception: {str(e)}")
        webbrowser.open("https://wa.me/17023565387?text=Hello%20%F0%9F%91%8B%20I%20want%20to%20use%20IG-BRUTEFORCE%20tool.%20Can%20I%20have%20the%20key%F0%9F%97%9D%EF%B8%8F")

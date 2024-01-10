from cryptography.fernet import Fernet
import webbrowser
import requests
import os
import sys

def load_key_from_file(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def save_key_to_file(key, key_file):
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    original_file_path = encrypted_file_path[:-4]  # Remove '.enc' extension
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)

def check_for_updates(current_version):
    repo_url = 'https://raw.githubusercontent.com/WHITEDH4CKER/IG-BRUTEFORCE/main/version.txt'

    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        latest_version = response.text.strip()
        return latest_version > current_version
    except requests.exceptions.RequestException as e:
        print(f"Error checking for updates: {str(e)}")
        return False

def ask_for_permission():
    user_response = input("Do you want to use this tool for educational purposes? (y/n): ").lower()
    return user_response == 'y'

if __name__ == "__main__":
    version_file_path = 'version.txt'
    current_version = '1.0'
    print(f"Current version: {current_version}")

    try:
        with open(version_file_path, 'r') as file:
            version_txt = file.read().strip()
            if version_txt != current_version:
                print("A new version is available.")
                user_input = input("Do you want to update? (y/n): ").lower()
                if user_input == 'y' or user_input == 'yes':
                    print("Updating...")
                    webbrowser.open("https://github.com/WHITEDH4CKER/IG-BRUTEFORCE")
                    sys.exit()
            else:
                print("You have the latest version.")
    except FileNotFoundError:
        print("Error: version.txt file not found. Continue with the current version.")

    permission_given = ask_for_permission()

    if not permission_given:
        print("Sorry, this script is only for educational purposes.")
        sys.exit()

    key_file = 'encryption_key.key'
    encrypted_script_path = 'reading.py.enc'

    if os.path.exists(key_file):
        # Load the key from the file for decryption
        encryption_key = load_key_from_file(key_file)
    else:
        user_key = input("Enter your key: ")
        try:
            encryption_key = user_key.encode()  # Ensure the key is in bytes
            cipher_suite = Fernet(encryption_key)
            save_key_to_file(encryption_key, key_file)
        except Exception as e:
            print(f"Invalid key: {str(e)}")
            webbrowser.open("https://wa.me/17023565387?text=Hello%20%F0%9F%91%8B%20I%20want%20to%20use%20IG-BRUTEFORCE%20tool.%20Can%20I%20have%20the%20key%F0%9F%97%9D%EF%B8%8F")
            sys.exit()

    encrypted_script_path = 'reading.py.enc'  # Replace with the actual path to your encrypted script file

    try:
        decrypt_file(encrypted_script_path, encryption_key)
        exec(open('reading.py').read())
    except Exception as e:
        print(f"Invalid key or decryption error: {str(e)}")
        webbrowser.open("https://wa.me/17023565387?text=Hello%20%F0%9F%91%8B%20I%20want%20to%20use%20IG-BRUTEFORCE%20tool.%20Can%20I%20have%20the%20key%F0%9F%97%9D%EF%B8%8F")
        sys.exit()

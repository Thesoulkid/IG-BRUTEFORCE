from cryptography.fernet import Fernet
import webbrowser
import requests
import os

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
    # Replace 'your-repo-url' with the URL of your GitHub repository's raw version file
    version_url = 'https://github.com/WHITEDH4CKER/IG-BRUTEFORCE/version.txt'

    try:
        response = requests.get(version_url)
        latest_version = response.text.strip()
        return latest_version > current_version
    except Exception as e:
        print(f"Error checking for updates: {str(e)}")
        return False

def ask_for_permission():
    user_response = input("Do you want to use this script for educational purposes? (y/n): ").lower()
    return user_response == 'y'

if __name__ == "__main__":
    current_version = '1.0'  # Replace with your current version
    print(f"Current version: {current_version}")

    if check_for_updates(current_version):
        user_input = input("A new version is available. Do you want to update? (y/n): ").lower()
        if user_input == 'y' or user_input == 'yes':
            print("Updating...")
            # Add your update logic here
            webbrowser.open("https://github.com/WHITEDH4CKER/IG-BRUTEFORCE")  # Open a browser or perform update steps
            exit()
        else:
            print("Continuing with the current version.")

    permission_given = ask_for_permission()

    if not permission_given:
        print("Sorry, this script is only for educational purposes.")
        exit()

    key_file = 'encryption_key.key'  # Specify the file to store the encryption key

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
            exit()

    encrypted_script_path = 'reading.py.enc'  # Replace with the actual path to your encrypted script file

    try:
        decrypt_file(encrypted_script_path, encryption_key)
        exec(open('reading.py').read())
    except Exception as e:
        print(f"Invalid key or decryption error: {str(e)}")
        webbrowser.open("https://wa.me/17023565387?text=Hello%20%F0%9F%91%8B%20I%20want%20to%20use%20IG-BRUTEFORCE%20tool.%20Can%20I%20have%20the%20key%F0%9F%97%9D%EF%B8%8F")

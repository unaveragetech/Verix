import json
import hashlib
import os
from cryptography.fernet import Fernet
import requests

USER_DATA_FILE = 'user_data.json'
KEY_FILE = 'secret.key'

# ---------------- Encryption & Decryption ---------------- #
# Generate or load the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, 'rb').read()

# Encrypt the API key
def encrypt_api_key(api_key):
    fernet = Fernet(load_key())
    return fernet.encrypt(api_key.encode()).decode()

# Decrypt the API key
def decrypt_api_key(encrypted_api_key):
    fernet = Fernet(load_key())
    return fernet.decrypt(encrypted_api_key.encode()).decode()

# ----------------- Password Hashing ---------------- #
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ----------------- Data Management ----------------- #
def save_user_data(email, encrypted_api_key, password):
    user_data = load_all_user_data()
    hashed_password = hash_password(password)
    user_data[email] = {'api_key': encrypted_api_key, 'password': hashed_password}
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(user_data, f)

def load_all_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def load_user_data(email):
    user_data = load_all_user_data()
    return user_data.get(email)

def delete_user_account(email):
    user_data = load_all_user_data()
    if email in user_data:
        del user_data[email]
        with open(USER_DATA_FILE, 'w') as f:
            json.dump(user_data, f)
        print(f"Account with email {email} has been deleted.")
    else:
        print(f"No account found for {email}.")

# ------------------ API Interaction ------------------ #
def get_api_key(email):
    url = f"https://formsubmit.co/api/get-apikey/{email}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching API key: {e}")
        return {}

def get_submissions(api_key):
    url = f"https://formsubmit.co/api/get-submissions/{api_key}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching submissions: {e}")
        return {}

# ------------------- Core Functions ------------------- #
def create_account():
    email = input("Enter your email to create an account: ")
    
    # Step 1: Get API key from FormSubmit
    api_response = get_api_key(email)
    if api_response.get("success"):
        print("API key sent to your email. Please check your mailbox.")
        api_key = input("Enter the API key you received in your email: ")

        # Step 2: Encrypt the API key for storage
        encrypted_api_key = encrypt_api_key(api_key)
        
        # Step 3: Set up a password for the account
        password = input("Set a password for your account: ")

        # Step 4: Save the encrypted API key and hashed password
        save_user_data(email, encrypted_api_key, password)
        print("Account created successfully! You can now log in.")
    else:
        print("Error:", api_response.get("message"))

def login_user():
    email = input("Enter your email to log in: ")
    user = load_user_data(email)
    if not user:
        print("No account found for this email. Please create an account first.")
        return None

    password = input("Enter your password: ")
    if hash_password(password) == user['password']:
        print("Login successful!")
        decrypted_api_key = decrypt_api_key(user['api_key'])
        return {'email': email, 'api_key': decrypted_api_key}
    else:
        print("Incorrect password.")
        return None

def fetch_submissions(user):
    api_key = user['api_key']
    submissions_response = get_submissions(api_key)
    if submissions_response.get("success"):
        submissions = submissions_response.get("submissions", [])
        if submissions:
            print("Your submissions:")
            for submission in submissions:
                print(f"Form URL: {submission['form_url']}")
                print(f"Submitted Data: {submission['form_data']}")
                print(f"Submitted At: {submission['submitted_at']['date']}")
                print("-" * 40)
        else:
            print("No submissions found.")
    else:
        print("Error:", submissions_response.get("message"))

def delete_account():
    email = input("Enter your email to delete your account: ")
    delete_user_account(email)

# -------------------- Main CLI Loop -------------------- #
def main():
    # Check if encryption key exists, otherwise generate one
    if not os.path.exists(KEY_FILE):
        generate_key()
    
    print("Welcome to the FormSubmit CLI Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Create Account (Get API Key)")
        print("2. Login and Get Submissions")
        print("3. Delete Account")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_account()

        elif choice == '2':
            user = login_user()
            if user:
                fetch_submissions(user)

        elif choice == '3':
            delete_account()

        elif choice == '4':
            print("Exiting the tool.")
            break

        else:
            print("Invalid choice. Please select again.")

# Run the main loop
if __name__ == '__main__':
    main()

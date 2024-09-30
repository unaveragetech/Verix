import requests
import random
import argparse
import hashlib
import time
import os

# Constants for FormSubmit
FORM_ACTIVATION_URL = "https://formsubmit.co/YOUR_RANDOM_STRING"  # Replace with FormSubmit's random string for invisible email
FORM_VERIFY_URL = "https://formsubmit.co/YOUR_RANDOM_STRING"  # Replace with FormSubmit's random string for invisible email

# Function to send the activation email
def send_activation_email(email):
    activation_data = {
        'email': email,
        '_subject': 'Activate your account',
        '_autoresponse': 'Please confirm activation of your account by clicking the activation link in your email.',
        '_captcha': 'false',  # Disable CAPTCHA to streamline the process
        '_next': 'https://yourdomain.com/activated.html'  # Redirect after activation
    }
    
    response = requests.post(FORM_ACTIVATION_URL, data=activation_data)
    
    if response.status_code == 200:
        print(f"Activation email sent to {email}. Check your inbox and confirm activation.")
    else:
        print(f"Failed to send activation email. Status code: {response.status_code}")

# Function to generate a verification code
def generate_verification_code():
    return random.randint(100000, 999999)

# Function to send the verification code email
def send_verification_email(email, name, code):
    verification_data = {
        'email': email,
        '_subject': 'Your verification code',
        'message': f'Hello {name},\nYour verification code is {code}. Please enter this to verify your account.',
        '_captcha': 'false'  # Disable CAPTCHA for seamless verification
    }
    
    response = requests.post(FORM_VERIFY_URL, data=verification_data)
    
    if response.status_code == 200:
        print(f"Verification email sent to {email}.")
    else:
        print(f"Failed to send verification email. Status code: {response.status_code}")

# Function to store user information in a file
def store_user_info(name, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_data = f"Name: {name}, Email: {email}, Password: {hashed_password}\n"
    
    with open("user_data.txt", "a") as file:
        file.write(user_data)
    
    print("User information stored successfully.")

# Function to verify user input
def verify_user_input(code):
    user_code = input("Enter the verification code you received: ")
    return str(user_code) == str(code)

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send email verification via FormSubmit.')
    parser.add_argument('email', type=str, help='Email address to send the verification.')
    parser.add_argument('name', type=str, help='User\'s account name.')
    
    args = parser.parse_args()
    
    # Step 1: Send activation email
    send_activation_email(args.email)
    
    # Prompt the user to confirm they have activated the form
    input("Once you've activated the form in your email, press Enter to continue...")
    
    # Step 2: Generate verification code
    code = generate_verification_code()
    
    # Step 3: Send verification code email
    send_verification_email(args.email, args.name, code)
    
    # Step 4: Verify the user's code input
    if verify_user_input(code):
        print("Account verified successfully!")
        
        # Step 5: Prompt for password and store user info
        password = input("Enter a password to use for your account: ")
        store_user_info(args.name, args.email, password)
    else:
        print("Verification failed. Incorrect code.")

# verix
# Email Verification with FormSubmit

This repository contains a Python script that adds email verification to any project using [FormSubmit](https://formsubmit.co). The system sends an activation email to the user, followed by a verification code that must be entered in the CLI. Once the user is verified, their account information is saved to a file.

## Features

- **Activation Email**: Sends an email to the provided address, requiring the user to activate the form via FormSubmit.
- **Verification Code**: After activation, a random 6-digit code is generated and emailed to the user for verification.
- **User Authentication**: Once the user enters the correct verification code, their information is securely stored, and they are prompted to set a password.
- **CLI Integration**: The script runs in a command-line interface for easy integration into any project.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_GITHUB_REPO/email-verification.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd email-verification
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the script, run it from the CLI with the user's email and name as arguments:

```bash
python email_verification.py user@example.com "John Doe"
Steps:
Activation Email: The user will receive an activation email from FormSubmit. They must click the activation link in their inbox to enable the form.

Verify Activation: After the user has activated the form, press Enter in the CLI to continue.

Verification Code: A verification code will be sent to the user's email. The user must enter the code in the CLI.

Password Setup: After successful verification, the user is prompted to set a password, which will be securely stored.

Example
bash
Copy code
python email_verification.py example@domain.com "Jane Doe"
Step 1: The user receives an activation email.
Step 2: The user verifies the form activation.
Step 3: The user receives a verification code and enters it into the CLI.
Step 4: The user's account is verified and stored.
FormSubmit Integration
The script uses FormSubmit's invisible email feature for added security, as well as their POST submission API to send emails. To ensure compliance with FormSubmit rules:

The email address is hidden using FormSubmit's random string in the FORM_ACTIVATION_URL and FORM_VERIFY_URL.
CAPTCHA is disabled for a smoother user experience.
Autoresponse messages and email subjects are set for both activation and verification emails.
Customization
You can modify the _next, _subject, and other hidden fields in the send_activation_email() and send_verification_email() functions to match your project needs.

For example, if you want to customize the "Thank You" page after form activation, change the _next field:

python
Copy code
'_next': 'https://yourdomain.com/activated.html'
Future Enhancements
File Upload: Allow users to upload files (e.g., profile images or ID cards) as part of their verification.
Webhooks: Integrate webhooks for real-time data manipulation on form submissions.
Contributing
If you have suggestions or find any issues, feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy code

---

### Additional Notes:
- Ensure you replace `YOUR_RANDOM_STRING` in the script with the actual random string provided by FormSubmit when you activate your form.
- The README outlines the purpose of the script, installation instructions, and usage examples, making it easy for others to integrate this functionality into their projects.

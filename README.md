
---

# Verix - Form Submission Backup Tool

This repository contains a Python tool designed to **back up all form submissions** sent to the email address you are checking. It uses the [FormSubmit](https://formsubmit.co) API to retrieve submissions linked to your FormSubmit forms, ensuring you have a reliable backup of all the data sent through your forms. 

**Note**: The FormSubmit API allows only **3 full requests per 24 hours**, so be mindful of this limit when making requests.

## Features

- **Form Submission Backup**: Retrieves and saves all form submissions sent to a specific email address using the FormSubmit API.
- **Encrypted API Key Storage**: API keys are securely encrypted and stored locally using industry-standard encryption.
- **Submission Search**: Allows you to search through the submissions for specific data fields (like names or emails).
- **Command-Line Interface (CLI)**: The entire tool runs in a CLI environment, making it easy to use and integrate with other projects.
- **User Authentication**: Provides password protection for accessing and managing submission data.

---

## How the Code Works

```bash
# 1. API Key Retrieval:
```
After providing your email, the tool requests an API key from FormSubmit. The API key is sent to the provided email address, and the user must enter it into the tool to verify ownership. The API key is then encrypted and stored locally.

```bash
# 2. Submissions Retrieval:
```
The tool uses the FormSubmit API to retrieve submissions linked to your form. The `get_submissions` function sends a GET request to the FormSubmit endpoint, fetching all forms submitted to the provided email address. The retrieved data is processed and displayed in the terminal.

```bash
# 3. Submission Search:
```
You can search through your form submissions using specific keywords. For example, if you're looking for a form submitted by "John Doe", you can enter the search term, and the tool will display all forms where this name appears.

```bash
# 4. Rate Limiting:
```
FormSubmit imposes a **limit of 3 full API requests per 24 hours**. Each request retrieves all form submissions tied to the email address. Be mindful of this restriction to avoid hitting the limit.

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/YOUR_GITHUB_REPO/verix-backup.git
```

### 2. Navigate to the project directory:
```bash
cd verix-backup
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

To use the tool, run the script from the CLI. You'll be prompted for your email address and API key, and the tool will then retrieve and display your form submissions.

### Example:

```bash
python verix.py
```

#### Steps:

1. **Enter Email**: Input the email address associated with your FormSubmit forms.
2. **Retrieve API Key**: The tool will guide you through requesting an API key from FormSubmit. Check your email, and enter the API key when prompted.
3. **View or Search Submissions**: After logging in, you can choose to either view all submissions or search for specific submissions based on keywords.
4. **Logout**: When you're done, you can log out, which will securely clear your session.

#### Example Command:

```bash
python verix.py
```

**Note**: Each API key request counts toward the daily limit of 3 API requests.

---

## FormSubmit API Integration

The tool integrates seamlessly with FormSubmit’s API to manage your form submissions. Below are some key details about how the API interaction works:

- **API Key**: Your API key is requested from FormSubmit and is used to fetch all the submissions linked to your form.
- **Request Limits**: The FormSubmit API allows up to **3 full requests per 24-hour period**. Each full request retrieves all available submissions.
- **Hidden Email**: For security purposes, the tool does not directly expose your email but uses the encrypted API key instead.
- **Form Data**: All form data, including names, emails, and messages submitted through your forms, is retrieved via the API.

---

## Code Walkthrough

```bash
# Core Functions:
```

- **`get_api_key(email)`**: This function sends a request to FormSubmit to retrieve the API key for the provided email. The key is then encrypted and stored for future use.
  
- **`get_submissions(api_key)`**: This function retrieves all submissions tied to the provided email address. It uses the encrypted API key to authenticate the request.

- **`search_submissions(api_key, search_term)`**: Allows users to search for specific data within the form submissions. This feature scans through all submissions and returns those that match the search term.

- **`encrypt_api_key(api_key)` / `decrypt_api_key(encrypted_api_key)`**: These functions handle the encryption and decryption of the API key to ensure that sensitive data is stored securely.

- **`loading_bar(duration)`**: Adds a loading bar for a smoother user experience while waiting for API requests to complete.

---

## Customization

You can customize certain aspects of the tool to fit your project’s needs. For example, if you want to customize the output format or add additional fields to be displayed, you can modify the output code in the `fetch_submissions()` and `search_submissions()` functions.

---

## Future Enhancements

- **Real-Time Submissions**: Implement real-time submission tracking by integrating with FormSubmit’s webhook system.
- **File Upload**: Allow users to upload files (such as profile images or documents) as part of the form submission process.

---

## Contributing

If you have suggestions for new features or bug fixes, feel free to submit a pull request or open an issue in the GitHub repository.

---

## License

This project is licensed under the SDUC License. For more details, see the `LICENSE` file in the repository.


```
TODO
Save Logic: Implement logic to save all information returned by the curl command used to fetch submissions from FormSubmit.
Improved Error Handling: Enhance error handling for API requests to provide more user-friendly error messages.
Automated Backups: Create a feature for scheduled automated backups of submissions at user-defined intervals.
Detailed Submission Logging: Log all submissions with timestamps and user details for better tracking.
Improved User Interface: Develop a more user-friendly interface for interacting with the tool, potentially adding a GUI.
Future Enhancements
The future of this project includes various enhancements to improve functionality and user experience:

Real-Time Submissions: Implement real-time submission tracking by integrating with FormSubmit’s webhook system.
File Upload: Allow users to upload files (such as profile images or documents) as part of the form submission process.
Custom Reports: Generate customizable reports based on submission data, allowing users to analyze trends and statistics easily.
Multi-Form Support: Enable the ability to manage multiple forms simultaneously within the tool, streamlining the backup process for users with several forms.
Mobile Compatibility: Develop a mobile version of the tool for users to manage their submissions on the go.

```
---

### Additional Notes

- Make sure to update the tool with your correct FormSubmit API details.
- The tool is rate-limited to **3 full requests per 24 hours**, so plan your usage accordingly.



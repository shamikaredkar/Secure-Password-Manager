# Secure Password Manager

A simple and secure password manager built with Python, utilizing the `cryptography` library to securely encrypt and decrypt passwords. This tool allows users to safely store and manage their passwords locally.

## Installation

Before you begin, ensure you have Python installed on your system. This project was developed with Python 3.9.18, but it should work with other versions with some compatibility.

### Dependencies

The project relies on the `cryptography` library. You can install it using pip:

`pip install cryptography`

If you encounter any issues with the installation, consider checking your Python interpreter or installing the library in a virtual environment.

### Usage

To start using the Secure Password Manager, you first need to generate an encryption key. This key will be used to encrypt your passwords and store them securely.
Run the write_key function to generate a key. This step is required only once, before the first use:

`write_key()  # Remember to comment this out after the first run`

With the key generated, you can now add and view passwords:
  1. To add a new password, run the program and select option 1.
  2. To view existing passwords, run the program and select option 2.

### Features
  1. Secure Encryption: Utilizes Fernet encryption from the cryptography library for secure password management.
  2. Easy to Use: Simple CLI interface for adding and viewing passwords.
  3. Local Storage: Passwords are stored locally in an encrypted format, ensuring your data stays private.

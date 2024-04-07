# Import the Fernet module from cryptography library for encryption and decryption purposes.
from cryptography.fernet import Fernet

# Function to generate and write a new encryption key to a file. 
# This should only be run once initially to create the key.
def write_key():
    # Generate a new Fernet encryption key.
    key = Fernet.generate_key()
    # Open or create 'key.key' file in write-binary ('wb') mode to store the encryption key.
    with open("key.key", "wb") as key_file:
        # Write the generated key to the file.
        key_file.write(key)

# Function to load the encryption key from the 'key.key' file.
def load_key():
    # Open the 'key.key' file in read-binary ('rb') mode.
    with open("key.key", "rb") as file:
        # Read the encryption key from the file.
        key = file.read()
    # Return the encryption key.
    return key

# Prompt the user to enter a master password. This is for demonstration and might be part of a more complex authentication process.
master_pwd = input("What is the master password? ")
# Uncomment the line below to generate a key if it hasn't been generated yet.
# write_key()

# Load the encryption key from the file and append the encoded master password to it.
# This approach of combining the key with a password is just for demonstration and not a standard practice.
key = load_key() + master_pwd.encode()
# Initialize the Fernet class with the combined key for encryption and decryption operations.
fer = Fernet(key)

# Function to view and decrypt passwords stored in 'passwords.txt'.
def view():
    # Open 'passwords.txt' in read mode.
    with open('passwords.txt', 'r') as f:
        # Iterate through each line in the file.
        for line in f.readlines():
            # Remove any trailing characters (like newlines) from the line.
            data = line.rstrip()
            # Split the line into username and password based on the '|' delimiter.
            user, pwd = data.split("|")
            # Decrypt the password and decode it to a string.
            decrypt = fer.decrypt(pwd.encode()).decode()
            # Print the account name and decrypted password.
            print(f"Account Name: {user} | Password: {decrypt}")
            
# Function to add a new password entry to 'passwords.txt'.
def add():
    # Prompt the user for the account name and password.
    name = input("Account name: ")
    pwd = input("Password: ")
    # Encrypt the password and decode it to a string.
    encrypt = fer.encrypt(pwd.encode()).decode()
    # Open 'passwords.txt' in append mode, which adds to the end of the file without overwriting it.
    with open('passwords.txt', 'a') as f:
        # Write the account name and encrypted password to the file, separated by a '|' delimiter.
        f.write(f"{name} | {encrypt} \n")
        

# Main loop to prompt the user for actions.
while True:
    # Prompt the user to choose an action: add a password, view passwords, or exit.
    mode = int(input("1. Would you like to add a new password \n 2. View existing passwords \n 3. Exit \n"))
    if mode == 1:
        # If the user chooses to add a password, call the add function.
        add()
    elif mode == 2:
        # If the user chooses to view passwords, call the view function.
        view()
    elif mode == 3:
        # If the user chooses to exit, break out of the loop and end the program.
        break
    else: 
        # If the user enters an invalid option, notify them and continue the loop.
        print("Invalid password, please try again.")


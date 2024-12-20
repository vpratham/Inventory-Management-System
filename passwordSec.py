import hashlib
import os

file_path = 'user_data.dat'
fp = 'ad.dat'


# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create or update a .dat file with username and hashed password
def store_user_credentials(username, password, file_path='user_data.dat'):
    hashed_password = hash_password(password)
    
    # Append to the .dat file
    with open(file_path, 'a') as file:
        file.write(f'{username}:{hashed_password}\n')

    #print(f"User '{username}' credentials stored successfully.")

# Function to check if the username already exists
def user_exists(username, file_path='user_data.dat'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(':')
                if stored_username == username:
                    return True
    return False

# Function to validate username and password
def validate_user(username, password):
    hashed_password = hash_password(password)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(':')
                if stored_username == username and stored_hashed_password == hashed_password:
                    return True
    return False

# Main function to create a new user
def create_user(username, password):
    if user_exists(username):
        print("Username already exists. Try a different one.")
        return
    # Store the hashed password in the .dat file
    store_user_credentials(username, password)


# Function to log in a user
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_user(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Testing the function
#create_user('manav079@company', 'zzM060lT@23)20xq')
#create_user('root','root')

#print(validate_user('root','root'))

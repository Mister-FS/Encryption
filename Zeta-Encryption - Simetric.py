from cryptography.fernet import Fernet

# Encrypting files with FERNET SYMMETRIC KEY CRYPTOGRAPHY
# Using AES 128 bit encryption - AES is Advanced Encryption Standard


# Generate a Key
# Key Required to encrypt and decrypt the file
#key = Fernet.generate_key()

# Saveing the key in a file
#with open("Key.key", "wb") as key_file:
    #key_file.write(key)

#print("Key has been generated and saved in key.key file")
#print("Please keep the key safe and secure")

# Function to load the key. 
def load_key():
    with open("Key.key", "rb") as key_file:
        return key_file.read()

# Loading the Key
key = load_key()
fernet = Fernet(key)

# Function to encrypt the file. 
def encrypting_file(file_name):
    # Encrypting and saving the file
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Encrypting Data
    encrypted_data = fernet.encrypt(file_data)

    # Saving the Encryted data in the original file
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

    print("File has been encrypted successfully")

#encrypting_file("image.jpg")


# Function to decrypt the file. 
def decrypting_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    # Reading Encrypted Data
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    # Decrypting Data
    original_data = fernet.decrypt(encrypted_data)

    # Saving the Decrypted data in the original file
    with open(file_name, "wb") as file:
        file.write(original_data)

#decrypting_file("image.jpg")
encrypting_file("image.jpg")
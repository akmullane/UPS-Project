from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
f = Fernet(key)

# Encrypt a message
message = b"Hello, world!"
encrypted_message = f.encrypt(message)

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message)

print("Original message: ", message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)

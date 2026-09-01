import random
import string

print("🔐 PASSWORD GENERATOR")
print("---------------------")

# Ask for password length
length = int(input("Enter password length: "))

# Ask what characters to include
use_uppercase = input("Include uppercase letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_special = input("Include special characters? (y/n): ").lower()

# Start with lowercase letters
characters = string.ascii_lowercase

# Add selected character types
if use_uppercase == "y":
    characters += string.ascii_uppercase

if use_numbers == "y":
    characters += string.digits

if use_special == "y":
    characters += string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nYour generated password is:")
print(password)
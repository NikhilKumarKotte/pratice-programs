import random
import string

print("🔐 SECURE PASSWORD GENERATOR")
print("----------------------------")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
    exit()

characters = string.ascii_lowercase
password = []

use_uppercase = input("Include uppercase? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_special = input("Include special characters? (y/n): ").lower()

# Always add one lowercase character
password.append(random.choice(string.ascii_lowercase))

if use_uppercase == "y":
    characters += string.ascii_uppercase
    password.append(random.choice(string.ascii_uppercase))

if use_numbers == "y":
    characters += string.digits
    password.append(random.choice(string.digits))

if use_special == "y":
    characters += string.punctuation
    password.append(random.choice(string.punctuation))

# Fill remaining characters
while len(password) < length:
    password.append(random.choice(characters))

# Shuffle password
random.shuffle(password)

password = "".join(password)

print("\n🔑 Generated Password:")
print(password)
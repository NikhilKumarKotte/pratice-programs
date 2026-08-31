import random

# Generate a random number
secret_number = random.randint(1, 100)

attempts = 7

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.\n")

for attempt in range(1, attempts + 1):

    try:
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

        if guess < 1 or guess > 100:
            print("❌ Please enter a number between 1 and 100.\n")
            continue

        if guess == secret_number:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempt} attempts!")
            break

        elif guess < secret_number:
            print("📈 Too low! Try a higher number.\n")

        else:
            print("📉 Too high! Try a lower number.\n")

    except ValueError:
        print("❌ Please enter a valid number.\n")

else:
    print("😢 Game Over!")
    print(f"The number was {secret_number}.")
import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("🪨 📄 ✂️ ROCK PAPER SCISSORS")

while True:

    player = input(
        "\nChoose rock, paper, scissors "
        "or type quit: "
    ).lower()

    if player == "quit":
        break

    if player not in choices:
        print("❌ Invalid choice!")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:

        print("🤝 It's a draw!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):

        print("🎉 You win!")
        player_score += 1

    else:

        print("💻 Computer wins!")
        computer_score += 1

    print(
        f"Score → You: {player_score} "
        f"Computer: {computer_score}"
    )

print("\nFinal Score")
print("You:", player_score)
print("Computer:", computer_score)
import random

board = [" "] * 9

def display_board():

    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner():

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if (
            board[a] != " " and
            board[a] == board[b] and
            board[b] == board[c]
        ):

            return board[a]

    if " " not in board:
        return "draw"

    return None


print("🧩 TIC-TAC-TOE")
print("You are X")
print("Computer is O")

while True:

    display_board()

    # Player
    while True:

        try:
            position = int(
                input("Choose a position (1-9): ")
            ) - 1

            if 0 <= position <= 8 and board[position] == " ":
                board[position] = "X"
                break

            print("❌ Invalid position!")

        except ValueError:

            print("Enter a number from 1 to 9.")

    result = check_winner()

    if result:
        break

    # Computer
    available = [
        i for i in range(9)
        if board[i] == " "
    ]

    computer_move = random.choice(available)

    board[computer_move] = "O"

    print("🤖 Computer played.")

    result = check_winner()

    if result:
        break

display_board()

if result == "X":

    print("🎉 You win!")

elif result == "O":

    print("🤖 Computer wins!")

else:

    print("🤝 It's a draw!")
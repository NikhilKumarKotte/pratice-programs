import random

player = {
    "name": "",
    "health": 100,
    "attack": 20,
    "gold": 50
}

print("⚔️ WELCOME TO THE RPG ⚔️")

player["name"] = input("Enter your hero's name: ")

print(f"\nWelcome, {player['name']}!")

enemies = [
    {"name": "Goblin", "health": 40, "attack": 10},
    {"name": "Orc", "health": 60, "attack": 15},
    {"name": "Dragon", "health": 100, "attack": 25}
]

while player["health"] > 0:

    print("\n----------------")
    print("1. Explore")
    print("2. Check stats")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":

        enemy = random.choice(enemies).copy()

        print(f"\n👹 A {enemy['name']} appeared!")

        while enemy["health"] > 0 and player["health"] > 0:

            print("\n1. Attack")
            print("2. Run")
            print("3. Use potion")

            action = input("Choose: ")

            if action == "1":

                damage = random.randint(
                    player["attack"] - 5,
                    player["attack"] + 5
                )

                enemy["health"] -= damage

                print(
                    f"⚔️ You dealt {damage} damage!"
                )

                if enemy["health"] > 0:

                    damage = random.randint(
                        enemy["attack"] - 3,
                        enemy["attack"] + 3
                    )

                    player["health"] -= damage

                    print(
                        f"💥 {enemy['name']} dealt "
                        f"{damage} damage!"
                    )

            elif action == "2":

                print("🏃 You escaped!")
                break

            elif action == "3":

                player["health"] += 25

                if player["health"] > 100:
                    player["health"] = 100

                print("❤️ You restored health!")

        if enemy["health"] <= 0:

            reward = random.randint(10, 50)
            player["gold"] += reward

            print(f"\n🎉 You defeated {enemy['name']}!")
            print(f"💰 You received {reward} gold.")

    elif choice == "2":

        print("\n📊 PLAYER STATS")
        print("Name:", player["name"])
        print("Health:", player["health"])
        print("Attack:", player["attack"])
        print("Gold:", player["gold"])

    elif choice == "3":

        print("Thanks for playing!")
        break

    else:

        print("Invalid choice!")

if player["health"] <= 0:
    print("\n💀 You died!")
import random

health = 100
gold = 0
potions = 2

rooms = [
    "Treasure Room",
    "Monster Room",
    "Trap Room",
    "Empty Room"
]

print("🏰 DUNGEON ADVENTURE")
print("Find treasure and survive!")

while health > 0:

    print("\n================")
    print("❤️ Health:", health)
    print("💰 Gold:", gold)
    print("🧪 Potions:", potions)

    print("\n1. Enter a room")
    print("2. Use potion")
    print("3. Leave dungeon")

    choice = input("Choose: ")

    if choice == "1":

        room = random.choice(rooms)

        print(f"\n🚪 You entered a {room}.")

        if room == "Treasure Room":

            treasure = random.randint(20, 100)

            gold += treasure

            print(f"💰 You found {treasure} gold!")

        elif room == "Monster Room":

            damage = random.randint(10, 30)

            health -= damage

            print(
                f"👹 A monster attacked you!"
                f"\nYou lost {damage} health."
            )

        elif room == "Trap Room":

            damage = random.randint(5, 20)

            health -= damage

            print(
                f"⚠️ You triggered a trap!"
                f"\nYou lost {damage} health."
            )

        else:

            print("Nothing happened...")

    elif choice == "2":

        if potions > 0:

            health += 30

            if health > 100:
                health = 100

            potions -= 1

            print("🧪 You used a potion.")

        else:

            print("You don't have any potions!")

    elif choice == "3":

        print("\n🏃 You escaped the dungeon!")
        break

    else:

        print("Invalid choice!")

if health <= 0:

    print("\n💀 You died in the dungeon.")

else:

    print("\n🎉 Adventure complete!")
    print("Final Gold:", gold)
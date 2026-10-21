# Setup the game
import random

# TASK 1
treasure = ["Gold coin", "Magic potion", "Diamond"]
monsters = ["Goblin", "Dragon", "Slime"]

print("Your treasure bag contains:", treasure)
print()

input("Press enter to start the game")
print()

# Add a treasure to the bag.
found_treasure = "Magic sword"
treasure.append(found_treasure)
print(f"You found a {found_treasure}!")
print("Your treasure bag contains:", treasure)
print()

# Pick a monster from the list.
# random.choice() selects one item at random.
monster = random.choice(monsters)

print(f"A wild {monster} appears!")
choice = input("Do you want to fight (F) or run away (R)? ")

# Give the player a different result depending on their choice.
score = 0

if choice == "F":
    print(f"You bravely face the {monster}!")
    # TASK 3
    
    print("You win a treasure for your bravery.")
    treasure.append("Monster gem")
    # TASK 2

elif choice == "R":
    print("You escape safely, but find no treasure this time.")
    # TASK 2

print()
print("QUEST RESULTS")
# Task 4
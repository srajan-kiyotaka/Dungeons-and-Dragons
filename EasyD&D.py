import random
from rich.pretty import pprint

print("Welcome to the D&D Adventure Game!")
print("You are a brave adventurer on a quest to defeat the evil wizard.")
print("You are currently in a dark forest and have several choices available to you:")
pprint({
    "1": "Continue forward",
    "2": "Go left",
    "3": "Go right",
    "4": "Search for items",
    "5": "Use magic"
})

hp = 100
mana = 50
inventory = []

while hp > 0:
    choice = input("What would you like to do? (1-5): ")

    if choice == "1":
        enemy = random.choice(["goblin", "ogre", "troll"])
        print("You have encountered a", enemy + ".")
        damage = random.randint(10, 30)
        hp -= damage
        print("The", enemy, "hit you for", damage, "points of damage.")
        print("You have", hp, "hit points remaining.")
    elif choice == "2":
        print("You have stumbled upon a small village.")
        print("You decide to rest and heal your wounds.")
        hp += 30
        print("You have recovered 30 hit points.")
        print("You now have", hp, "hit points.")
    elif choice == "3":
        print("You have found a hidden path leading to the evil wizard's castle.")
        break
    elif choice == "4":
        item_found = random.choice(["health potion", "mana potion", "sword", "shield"])
        inventory.append(item_found)
        print("You have found a", item_found + ".")
        print("Your inventory now contains:", inventory)
    elif choice == "5":
        if "mana potion" in inventory:
            mana += 30
            inventory.remove("mana potion")
            print("You have used a mana potion and gained 30 mana points.")
            print("You now have", mana, "mana points.")
        elif mana >= 20:
            enemy = random.choice(["goblin", "ogre", "troll"])
            damage = random.randint(30, 50)
            mana -= 20
            print("You have cast a spell and dealt", damage, "points of damage to the", enemy + ".")
            print("You now have", mana, "mana points remaining.")
        else:
            print("You do not have enough mana to cast a spell.")
    else:
        print("Invalid choice, try again.")

if hp > 0:
    print("You have reached the evil wizard's castle.")
    print("You engage in a final battle with the wizard.")
    if random.random() < 0.5:
        print("You have defeated the evil wizard and saved the land!")
    else:
        print("The wizard was too powerful for you and you have died.")
else:
    print("You have died in the forest.")

print("The end.")

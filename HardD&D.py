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
enemies_defeated = 0

while hp > 0:
    choice = input("What would you like to do? (1-5): ")

    if choice == "1":
        enemy = random.choice(["goblin", "ogre", "troll", "dragon", "minotaur"])
        print("You have encountered a", enemy + ".")
        damage = random.randint(10, 50)
        hp -= damage
        print("The", enemy, "hit you for", damage, "points of damage.")
        print("You have", hp, "hit points remaining.")
        if hp <= 0:
            break
        if random.random() < 0.5:
            print("You have defeated the", enemy + ".")
            enemies_defeated += 1
            if enemies_defeated == 3:
                print("You have defeated enough enemies to level up.")
                hp += 50
                mana += 30
                print("Your hit points have increased to", hp, "and your mana has increased to", mana + ".")
        else:
            print("You have fled from the", enemy + ".")
    elif choice == "2":
        if random.random() < 0.5:
            print("You have stumbled upon a small village.")
            print("You decide to rest and heal your wounds.")
            hp += 30
            print("You have recovered 30 hit points.")
            print("You now have", hp, "hit points.")
        else:
            print("You have stumbled upon a trap and taken damage.")
            damage = random.randint(20, 40)
            hp -= damage
            print("You have taken", damage, "points of damage.")
            print("You now have", hp, "hit points.")
    elif choice == "3":
        if enemies_defeated < 3:
            print("You must defeat at least three enemies before you can reach the evil wizard's castle.")
        else:
            print("You have found a hidden path leading to the evil wizard's castle.")
            break
    elif choice == "4":
        item_found = random.choice(["health potion", "mana potion", "sword", "shield", "amulet of power"])
        inventory.append(item_found)
        print("You have found a", item_found + ".")
        print("Your inventory now contains:", inventory)
    elif choice == "5":
        if "mana potion" in inventory:
            mana += 30
            inventory.remove("mana potion")
            print("You have used a mana potion and gained 30 mana points.")
            print("You

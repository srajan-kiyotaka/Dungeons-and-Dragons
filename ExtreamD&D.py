import random
from rich.pretty import pprint

class Character:
    def __init__(self, name, char_class, hp, mana, strength, intelligence, dexterity):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name}\nClass: {self.char_class}\nHP: {self.hp}\nMana: {self.mana}\nStrength: {self.strength}\nIntelligence: {self.intelligence}\nDexterity: {self.dexterity}\nInventory: {self.inventory}"

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated.")
            return False
        return True

    def attack(self, enemy):
        damage = self.strength + random.randint(1, 6)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        return enemy.take_damage(damage)

    def cast_spell(self, enemy):
        if self.mana < 10:
            print(f"{self.name} does not have enough mana to cast a spell.")
            return
        damage = self.intelligence + random.randint(1, 6)
        self.mana -= 10
        print(f"{self.name} casts a spell on {enemy.name} for {damage} damage.")
        return enemy.take_damage(damage)

    def use_item(self, item):
        if item not in self.inventory:
            print(f"{self.name} does not have the item {item}.")
            return
        if item == "health potion":
            self.hp += 20
            print(f"{self.name} uses a health potion and recovers 20 hit points.")
        elif item == "mana potion":
            self.mana += 20
            print(f"{self.name} uses a mana potion and recovers 20 mana points.")
        self.inventory.remove(item)

def generate_enemy():
    enemy_type = random.choice(["goblin", "ogre", "troll", "dragon", "minotaur"])
    enemy_stats = {
        "goblin": (30, 10, 5, 5),
        "ogre": (50, 5, 10, 3),
        "troll": (70, 5, 15, 2),
        "dragon": (100, 20, 20, 10),
        "minotaur": (80, 10, 20, 8)
    }
    hp, mana, strength, intelligence = enemy_stats[enemy_type]
    return Character(enemy_type, "Enemy", hp, mana, strength, intelligence, random.randint(1, 6))

def main():
    player = Character("Player", "Warrior", 100, 50, 20, 10, 15)
    player.inventory = ["health potion", "mana potion", "mana potion"]
    enemy = generate_enemy()
    print("An enemy has appeared!")
    pprint(enemy)

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} has {player.hp} hit points and {player.mana} mana.")
        print(f"{enemy.name} has {enemy.hp} hit points.")
        print("What would you like to do?\n1. Attack\n2. Cast spell\n3. Use item\n4. Show inventory")
        choice = int(input("> "))

        if choice == 1:
            if player.attack(enemy):
                enemy.attack(player)
        elif choice == 2:
            player.cast_spell(enemy)
            enemy.attack(player)
        elif choice == 3:
            print(f"What item would you like to use?\n{player.inventory}")
            item = input("> ")
            player.use_item(item)
            enemy.attack(player)
        elif choice == 4:
            print(f"{player.name}'s inventory: {player.inventory}")
        else:
            print("Invalid choice.")
    
    if player.hp > 0:
        print(f"{player.name} has defeated the {enemy.name}!")
    else:
        print(f"{player.name} has been defeated by the {enemy.name}.")

if __name__ == "__main__":
    main()

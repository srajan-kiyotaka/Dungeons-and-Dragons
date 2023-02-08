import java.util.Scanner;
import java.util.Random;

public class DnD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome to Dungeons & Dragons!");
        System.out.print("Enter your character name: ");
        String characterName = sc.nextLine();
        System.out.print("Enter your character's strength (1-20): ");
        int strength = sc.nextInt();
        System.out.print("Enter your character's dexterity (1-20): ");
        int dexterity = sc.nextInt();
        System.out.print("Enter your character's constitution (1-20): ");
        int constitution = sc.nextInt();

        Character character = new Character(characterName, strength, dexterity, constitution);
        System.out.println("Character created: " + character);

        while (true) {
            System.out.println("\nMain Menu:");
            System.out.println("1. Roll Dice");
            System.out.println("2. Engage in Combat");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            if (choice == 0) {
                break;
            } else if (choice == 1) {
                System.out.print("Enter the type of dice to roll (4, 6, 8, 10, 12, 20): ");
                int diceType = sc.nextInt();
                int diceRoll = random.nextInt(diceType) + 1;
                System.out.println(character.getName() + " rolled a " + diceRoll + " with a " + diceType + "-sided die.");
            } else if (choice == 2) {
                System.out.print("Enter the strength of the enemy: ");
                int enemyStrength = sc.nextInt();
                int attackRoll = random.nextInt(20) + 1 + character.getStrength();
                if (attackRoll > enemyStrength) {
                    System.out.println(character.getName() + " hits the enemy!");
                } else {
                    System.out.println(character.getName() + " misses the enemy.");
                }
            } else {
                System.out.println("Invalid choice. Try again.");
            }
        }
    }
}

class Character {
    private String name;
    private int strength;
    private int dexterity;
    private int constitution;

    public Character(String name, int strength, int dexterity, int constitution) {
        this.name = name;
        this.strength = strength;
        this.dexterity = dexterity;
        this.constitution = constitution;
    }

    public String getName() {
        return name;
    }

    public int getStrength() {
        return strength;
    }

    public int getDexterity() {
        return dexterity;
    }

    public int getConstitution() {
        return constitution;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Strength: " + strength + ", Dexterity: " + dexterity + ", Constitution: " + constitution;
    }


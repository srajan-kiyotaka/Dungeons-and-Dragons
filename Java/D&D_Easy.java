import java.util.Scanner;
import java.util.Random;

public class DnD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome to Dungeons & Dragons!");
        System.out.print("Enter your character name: ");
        String characterName = sc.nextLine();

        Character character = new Character(characterName);
        System.out.println("Character created: " + character);

        while (true) {
            System.out.print("Enter the type of dice to roll (4, 6, 8, 10, 12, 20, or 0 to exit): ");
            int diceType = sc.nextInt();
            if (diceType == 0) {
                break;
            }

            int diceRoll = random.nextInt(diceType) + 1;
            System.out.println(character.getName() + " rolled a " + diceRoll + " with a " + diceType + "-sided die.");
        }
    }
}

class Character {
    private String name;

    public Character(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}

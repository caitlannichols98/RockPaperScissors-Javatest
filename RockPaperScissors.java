import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        //A Scanner in Java is a class used to obtain input from various sources.
        //in this case, is the user input from the console.
        Scanner scans = new Scanner(System.in);

        Random randomize = new Random();
        int computerChoice = randomize.nextInt(3) + 1;

        //system out means computer is talking to USER. think third person. 
        //this is to prompt the user to enter their choice
        System.out.println("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors):");
        int userChoice = scans.nextInt();
        System.out.println("Computer's choice: " + convertToChoice(computerChoice));
        System.out.println("Your choice: " + convertToChoice(userChoice));

        String result = determineTheWinner(computerChoice, userChoice);
        System.out.println(result);

        scans.close();
    }

    // Method to convert numeric choices to A string. 
    //By the way, for future reference to oneself. switches are much better than a bunch of "If/then" on repeat.
    public static String convertToChoice(int choice) {
        switch (choice) {
            case 1:
                return "Rock";
            case 2:
                return "Paper";
            case 3:
                return "Scissors";
            default:
                return "Invalid choice";
        }
    }

    public static String determineTheWinner(int computer, int user) {
        if (computer == user) {
            return "It's a tie!";
        } else if ((computer == 1 && user == 3) || (computer == 2 && user == 1) || (computer == 3 && user == 2)) {
            return "Computer wins!";
        } else {
            return "You win!";
        }
    }

    private static String determineWinner(int computerChoice, int userChoice) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}

import sys
import random

def play_game(): #this is a "class" or rather, the classroom from java 
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    possible_actions = tuple(beats.keys()) #this pulls the function variable
 
    while True: #this is the function or a "teacher" from java
        #the line below this is the name of said "student" who will perform the instructions aka a variable
        print("Hi, welcome to rock, paper, scissors. This was manually persed from my java file. Please select one of these: rock, paper, scissors or type 'quit' to exit the game")
        user_action = input().strip().lower() #.lower means everything will now be lowercased in the input to not throw code off. the .strip removes unintended white space

        if user_action == 'quit':
            print("thanks for playing!")
            break
        if user_action not in possible_actions:
            print("Invalid input. Please enter 'rock', 'paper', 'scissors', 'quit'.")
            continue

        #possible_actions = ["rock", "paper", "scissors"] #the brackets in this case is considered a list []
        
        
        computer_action = random.choice(possible_actions) #like system print out, this is a computer part. it will also parentheses to house the "arguments" or parameter list of a function
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") #string with f uses the variable within string using {}. This works like str.format(), but in a more concise and readable way. 
        #f's end with \n typically

        #if (user_action == computer_action):
         #   print = ("its a tie!")
        #elif (user_action == "rock" & computer_action == "scissors") and (user_action == "scissors" & computer_action == "paper") and (user_action == "paper" & computer_action == "rock"):
         #   print: (f"you chose {user_action} and the opponent chose {computer_action}, Congrats you win!")
        #else:
         #   print:(f"you chose {user_action} and the opponent chose {computer_action}, the opponent wins!")    

        play_again = input("would you like to play again?: Y/N")
        if play_again == "yes" and "Y" and "y":
            continue
        else:
            break

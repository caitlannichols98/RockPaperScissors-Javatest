import random

beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
possible_actions = ["rock", "paper", "scissors"]

def play_game():
    print ("Hi,welcome to rock, paper, scissors.")
    print ("This was manually persed from my java file.")
    print ("Please select: rock, paper, scissors or type 'quit' to exit")

    while True:
        user_action = input("").strip().lower()
        if user_action == 'quit':
            print("Thanks for playing!")
            break

        if user_action not in possible_actions:
            print("Invalid input. Please enter rock, paper, scissors, or type quit.")
            continue

        computer_action = random.choice(possible_actions)

        if computer_action == user_action:
            result = "it is a tie!"
        elif beats[user_action] == computer_action:
            result = "You win!"
        else:
            result = "You lost..."

        print(f"You chose {user_action}, computer chose {computer_action}. Result: {result}") 

if __name__ == "__main__":
            play_game()

import random

while True:
    User_action = input("Enter a choice(rock, paper, scissors):").lower()
    possible_actions = ["rock", "paper", "scissors"]
    Computer_action = random.choice(possible_actions)
    print(f"\nYou chose {User_action}, computer chose {Computer_action}.\n")
    if User_action == Computer_action:
            print(f"Both players selected {User_action}. It's a tie!")
    elif User_action == "rock":
            if Computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
            else:
                    print("Paper covers rock! You lose.")
    elif User_action == "paper":
            if Computer_action == "rock":
                    print("Paper covers rock! You win!")
            else:
                    print("Scissors cuts paper! You lose.")
    elif User_action == "scissors":
            if Computer_action == "paper":
                    print("Scissors cuts paper! You win!")
            else:
                    print("Rock smashes scissors! You lose.")
    play_again = (input("Play again? (y/n):"))
    if play_again.lower() != "y":
            break
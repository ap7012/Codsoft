import random
while True:
    user = input("Enter a choice from rock, paper and scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choose {user}, computer choose {computer_action}.\n")

    if user == computer_action:
        print(f"Both players selected {user}. Its a tie!")
        
    elif user == "rock":
        if computer_action == "scissors":
            print("You win!!!")
        else:
            print("You lose.")
            
    elif user == "paper":
        if computer_action == "rock":
            print("You win!!!")
        else:
            print("You lose.")
            
    elif user == "scissors":
        if computer_action == "paper":
            print("You win!!!")
        else:
            print("You lose.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

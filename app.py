import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid choice. Please try again.")

def main():
    player_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"\nPlayer score: {player_score}")
        print(f"Computer score: {computer_score}\n")

        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
import random

def play_game():
    choices = ["rock", "parchment", "shears"]

    while True:
        print("\nWelcome to The Rock, Parchment, Shears Game!!!")
        print("Enter your choice: ")
        print("1. Rock")
        print("2. Parchment")
        print("3. Shears")
        print("4. EXIT THE GAME")

        user_selection = input("Enter your choice (1-4): ")

        if user_selection == "4":
            print("Thanks for playing!")
            break
        elif user_selection not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        user_choice = int(user_selection) - 1
        computer_choice = random.randint(0, 2)

        print("You chose:", choices[user_choice])
        print("Computer chose:", choices[computer_choice])

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            print("You win 🏆🏅!")
        else:
            print("Computer wins! 🙁\nBetter luck next time 🤞")

if __name__ == "__main__":
    play_game()

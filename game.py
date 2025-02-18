# # importing the random module to generate with the computer choices
# import random
#
# # while loop to recognise if the user has inputted R,P, or S
# def game():
#     player_input = input("Enter R for Rock, P for Paper, S for Scissors: ")
#     # player input variable is used to prompt the user to enter their choice
#     choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
#     # the dictionary helps to change the letter into the corresponding word
#
#     player_choice = input("Please choose Rock (R), Paper (P) or Scissors(S):")
#
# # Game will not play unless options are one of the above
# while player_choice not in options:
#     player_choice = input("Please enter either R, P or S:")
#
# # using the random choice function to generate a choice
# computer_choice = random.choice(options)
#
# # FUNCTIONS:
# def play_game (player_choice):
#     choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
#     computer_choice = random.choice(options)
#
#     if player_choice == computer_choice
#         return"You have tied!"

import random


def get_user_choice():
    """Prompt the user to enter a choice and return the corresponding value."""
    choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").strip().upper()
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    return choices.get(choice, None)


def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)


def determine_winner(user, computer):
    """Determine the winner based on user and computer choices."""
    if user == computer:
        return "It's a draw!"

    winning_combinations = {
        'Rock': 'Scissors',  # Rock beats Scissors
        'Paper': 'Rock',  # Paper beats Rock
        'Scissors': 'Paper'  # Scissors beats Paper
    }

    if winning_combinations[user] == computer:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """Main function to run the game."""
    user_choice = get_user_choice()
    if not user_choice:
        print("Invalid input. Please enter R, P, or S.")
        return

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


# Run the game
play_game()

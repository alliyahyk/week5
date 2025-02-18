# importing the random module to generate computer choices
import random

def get_user_choice():
    """Prompt user to enter R, P, or S and return the corresponding choice."""
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    user_input = input("Enter R for Rock, P for Paper, S for Scissors: ").strip().upper()
    return choices.get(user_input, None)


def get_computer_choice():
    """Generate a random number (0-2) and convert it to Rock, Paper, or Scissors."""
    choice_mapping = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
    return choice_mapping[random.randint(0, 2)]


def determine_winner(user, computer):
    """Compare choices and determine the game result."""
    if user == computer:
        return "It's a draw!"

    winning_combinations = {
        'Rock': 'Scissors',  # Rock smashes Scissors
        'Paper': 'Rock',  # Paper wraps Rock
        'Scissors': 'Paper'  # Scissors cut Paper
    }

    return "You win!" if winning_combinations[user] == computer else "You lose!"


def play_game():
    """Run the game loop."""
    user_choice = get_user_choice()
    if not user_choice:
        print("Invalid input! Please enter R, P, or S.")
        return

    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    print(determine_winner(user_choice, computer_choice))


# Run the game
play_game()

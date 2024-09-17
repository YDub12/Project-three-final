import random 

# Constants
BOARD_SIZE = 5
SHIP_SIZES = [3, 2, 1, 1]

# Symbols for the board
EMPTY_SYMBOL = '0'
SHIP_SYMBOL = 'S'
HIT_SYMBOL = 'H'
MISS_SYMBOL = 'M'

# Create an empty board

# Welcome message 
def welcome_message(username):
    print(f"Welcome Admiral {username}, to Battleships!\n")
    print(f"You will be playing on a {BOARD_SIZE}X{BOARD_SIZE} grid.\n")
    print("Your goal is to sink all of your opponents ships. \n")
    print("You will do this by making guesses below.")

# Main function
def main():
    # Get username 
    username = input("Enter your username here: ")
    welcome_message(username)


if __name__ == "__main__":
    main()
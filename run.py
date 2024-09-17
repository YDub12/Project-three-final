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
def create_board():
    return[[EMPTY_SYMBOL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    print("Debugging check")
    for row in board:
        print(" ".join(row))
    return board

# Welcome message 
def welcome_message(username):
    print(f"Welcome Admiral {username}, to Battleships!\n")
    print(f"You will be playing on a {BOARD_SIZE}X{BOARD_SIZE} grid.\n")
    print("Your goal is to sink all of your opponents ships. \n")
    print("You will do this by making guesses below.")

# Main function
def main():
    # Get username and print Welcome
    username = input("Enter your username here: ")
    welcome_message(username)

    # Create board 
    player_board = create_board()
    computer_board = create_board()

    


if __name__ == "__main__":
    main()
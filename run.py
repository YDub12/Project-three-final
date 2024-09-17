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

# Game selection menu
def select_game_type():
    print("Select Game Type:\n")
    print("1. Play against Computer")
    print("2. Play Local Multiplier")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        print(f"Debugging: User input is '{choice}'")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please choose 1, 2 or 3.")

# Game start functions 
# Check if a ship can be placed at the specified location
def valid_placement(board, row, col, size, orientation):
    if orientation == 'H':
        if col + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[row][col + i] != EMPTY_SYMBOL:
                return False
    else:
        if row + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[row + i][col] != EMPTY_SYMBOL:
                return False
    return True


# Main function
def main():
    # Get username and print Welcome
    username = input("Enter your username here: ")
    welcome_message(username)

    game_type = select_game_type()

    # Create board 
    player_board = create_board()
    computer_board = create_board()




if __name__ == "__main__":
    main()
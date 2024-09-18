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

# Display the board (hide ships unless show_ships is True)
def print_board(board, show_ships=False):
    print("  " + " ".join([str(i) for i in range(BOARD_SIZE)]))  # Column numbers
    for idx, row in enumerate(board):
        display_row = []
        for cell in row:
            if cell == SHIP_SYMBOL and not show_ships:
                display_row.append(EMPTY_SYMBOL)
            else:
                display_row.append(cell)
        print(f"{idx} " + " ".join(display_row))  # Row number

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

# Place a single ship on the board
def place_ship(board, row, col, size, orientation):
    for i in range(size):
        if orientation == 'H':
            board[row][col + i] = SHIP_SYMBOL
        else:
            board[row + i][col] = SHIP_SYMBOL

# Let the player manually place ships 
def player_place_ships(board):
    print("\nPlace your ships on the board.")
    for size in SHIP_SIZES:
        while True:
            try:
                print_board(board, show_ships=True)
                print(f"\nPlace your ship of size {size}.")
                row = int(input(f"Enter the starting row (0-{BOARD_SIZE-1}): "))
                col = int(input(f"Enter the starting column (0-{BOARD_SIZE-1}): "))
                orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()

                if orientation not in ['H', 'V']:
                    print("Invalid orientation. Please choose H or V.")
                    continue

                if valid_placement(board, row, col, size, orientation):
                    place_ship(board, row, col, size, orientation)
                    break
                else:
                    print("Invalid placement. The ship cannot go off the board or overlap with other ships.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for row and column.")

# Randomly place ships on the board (for computer)
def add_computer_ships(board):
    for size in SHIP_SIZES:
        while True:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, BOARD_SIZE - 1)
                col = random.randint(0, BOARD_SIZE - size)
            else:  # 'V'
                row = random.randint(0, BOARD_SIZE - size)
                col = random.randint(0, BOARD_SIZE - 1)

            if is_valid_placement(board, row, col, size, orientation):
                place_ship(board, row, col, size, orientation)
                break

# Main function
def main():
    # Get username and print Welcome
    username = input("Enter your username here: ")
    welcome_message(username)

    game_type = select_game_type()

    # Create board 
    player_board = create_board()
    computer_board = create_board()

    # Display board
    print("Player's Board:")
    print_board(player_board)
    print("Computer's Board(hidden ships):")
    print_board(computer_board)

    # Player places ships
    print(f"\n{username}, it's time to place your ships.")
    player_place_ships(player_board)
    
     # Computer places ships
    print("Computer is placing its ships...")
    add_computer_ships(computer_board)

if __name__ == "__main__":
    main()
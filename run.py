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
    return [[EMPTY_SYMBOL for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)]


# Display the board (hide ships unless show_ships is True)
def print_board(board, show_ships=False):
    print("  " + " ".join([str(i) for i in range(BOARD_SIZE)]))
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
        choice = input("Enter your choice (1/2/3):\n ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please choose 1, 2 or 3.")


# Game start functions
# Check if a ship can be placed at the specified location
def valid_placement(board, row, col, size, orientation):
    # Ensure the starting position is within bounds
    if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
        return False
    if orientation == 'H':
        if col + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[row][col + i] != EMPTY_SYMBOL:
                return False
    else:  # Orientation 'V'
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
                row = int(input(f"Enter the starting row
                          (0-{BOARD_SIZE-1}): \n"))
                col = int(input(f"Enter the starting column
                          (0-{BOARD_SIZE-1}): \n "))
                orientation = input("Enter orientation(H for horizontal,
                                    V for vertical): \n").upper()

                if orientation not in ['H', 'V']:
                    print("Invalid orientation. Please choose H or V.")
                    continue

                if valid_placement(board, row, col, size, orientation):
                    place_ship(board, row, col, size, orientation)
                    break
                else:
                    print("Invalid placement.
                          The ship cannot go off the board
                          or overlap with other ships.")
            except ValueError:
                print("Invalid input.
                      Please enter valid numbers for row and column.")


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

            if valid_placement(board, row, col, size, orientation):
                place_ship(board, row, col, size, orientation)
                break


# Get player's guess
def get_player_guess(guesses):
    while True:
        try:
            guess = input("Enter your guess
                          (row and column separated by space): \n ")
            row, col = map(int, guess.strip().split())
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print(f"Please enter numbers between 0 and {BOARD_SIZE - 1}.")
                continue
            if (row, col) in guesses:
                print("You have already guessed that location. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input format.
                  Please enter two numbers separated by space.")


# Check if a guess is a hit or miss
def check_guess(board, row, col):
    if board[row][col] == SHIP_SYMBOL:
        board[row][col] = HIT_SYMBOL
        print("Hit!")
        return True
    else:
        board[row][col] = MISS_SYMBOL
        print("Miss!")
        return False


# Check if all ships are sunk
def all_ships_sunk(board):
    return all(SHIP_SYMBOL not in row for row in board)


# Computer guess
def computer_guess(player_board, guesses):
    while True:
        row, col = random.randint(0, BOARD_SIZE - 1),
        random.randint(0, BOARD_SIZE - 1)
        if (row, col) not in guesses:
            guesses.add((row, col))
            print(f"Computer's guess: {row} {col}")
            return row, col


# Main game loop for playing against the computer
def play_against_computer(player_board, computer_board):
    player_guesses = set()
    computer_guesses = set()
    attempts = 0

    while True:
        # Player's turn
        print("Your turn to guess:")
        print("\nCurrent Board:")
        print_board(computer_board)
        row, col = get_player_guess(player_guesses)
        player_guesses.add((row, col))
        check_guess(computer_board, row, col)
        attempts += 1

        if all_ships_sunk(computer_board):
            print("Congratulations! You've sunk all of the computer's ships")
            break

        # Computer's turn
        print("\nComputer is guessing...")
        computer_row, computer_col = computer_guess(player_board,
                                                    computer_guesses)
        check_guess(player_board, computer_row, computer_col)

        if all_ships_sunk(player_board):
            print("The machines will take over after this. Well done.")
            break

        # Show the player's board after the computer's guess
        print("\nYour Board (after computer's guess):")
        print_board(player_board, show_ships=True)

    print("\nGame Complete")
    print(f"It took you {attempts} attempts.")
    print("\nFinal Board:")
    print_board(computer_board, show_ships=True)


# Main function
def main():
    # Get username with validation (non-empty and max 10 characters)
    while True:
        username = input("Enter your username (max 10 characters):\n ").strip()

        if len(username) < 3:
            print("Username must be at least 3 characters long.
                  Please enter a longer name.")
        elif len(username) > 10:
            print("Username cannot exceed 10 characters.
                  Please enter a shorter name.")
        else:
            break  # Exit the loop once a valid username is entered

    while True:  # This loop keeps the menu selection active
        game_type = select_game_type()
        if game_type == 3:
            print("Exiting game. Goodbye!")
            return  # Exit the program
        elif game_type == 1:
            # Play against computer
            player_board = create_board()
            computer_board = create_board()

            print("Computer is placing its ships...")
            add_computer_ships(computer_board)

            print("It's time to place your ships.")
            player_place_ships(player_board)

            # Change show_ships to True to display computer's board
            print("Computer's Board:")
            print_board(computer_board, show_ships=False)

            play_against_computer(player_board, computer_board)

            # After the game ends, return to the main menu
            print("\nReturning to the main menu...\n")

        elif game_type == 2:
            print("Local Multiplayer is under development.
                  Returning to menu...")


if __name__ == "__main__":
    main()

def tower_breakers(n, m):
    # Initialize the towers to height m
    towers = [m] * n

    # Function to display the current state of the towers
    def display_towers():
        for index, height in enumerate(towers, start=1):
            print(f"Tower {index}: {'|' * height} ({height})")

    # Function to perform the player's move
    def player_move():
        while True:
            try:
                tower_index = int(input("Enter the tower number you want to reduce: ")) - 1
                new_height = int(input(f"Enter the new height for Tower {tower_index + 1} (current height: {towers[tower_index]}): "))
                if 0 <= tower_index < len(towers) and 0 < new_height < towers[tower_index]:
                    towers[tower_index] = new_height
                    return True
                else:
                    print("Invalid move. Please choose an existing tower and a valid new height.")
            except ValueError:
                print("Please enter valid integer values for the tower number and height.")
            except IndexError:
                print("Please choose a valid tower number.")

    # Function to perform the computer's move
    def computer_move():
        for index, height in enumerate(towers):
            if height > 1:
                print(f"Computer reduces Tower {index + 1} from height {height} to 1.")
                towers[index] = 1
                return

    # Function to check for a winner
    def check_winner(player_turn):
        if all(height == 1 for height in towers):
            if player_turn:
                print("All towers are at height 1. The player wins!")
            else:
                print("All towers are at height 1. The computer wins!")
            return True
        return False

    # Main game loop
    player_turn = True
    while True:
        display_towers()
        if check_winner(player_turn):
            break

        if player_turn:
            print("Player's turn:")
            if not player_move():
                print("Invalid move. Please try again.")
                continue
        else:
            print("Computer's turn:")
            computer_move()

        player_turn = not player_turn

# Start the game
if __name__ == "__main__":
    n = int(input("Enter the number of towers: "))
    m = int(input("Enter the initial height of the towers: "))
    tower_breakers(n, m)

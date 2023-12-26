def tower_breakers(n, m):
    towers = [m] * n
    p1_turn = True  # True if it's P1's turn, False for P2's turn

    while True:
        # Display the current state of the towers
        for index, height in enumerate(towers, start=1):
            print(f"Tower {index}: {'|' * height} ({height})")

        # Check if all towers are of height 1
        if all(height == 1 for height in towers):
            if p1_turn:
                print("All towers are at height 1. P1 wins!")
                return "P1"
            else:
                print("All towers are at height 1. P2 wins!")
                return "P2"

        if p1_turn:
            print("P1's turn:")
            while True:
                try:
                    tower_index = int(input("Enter the tower number you want to reduce: ")) - 1
                    new_height = int(input(f"Enter the new height for Tower {tower_index + 1} (current height: {towers[tower_index]}): "))
                    if 0 <= tower_index < len(towers) and 0 < new_height < towers[tower_index]:
                        towers[tower_index] = new_height
                        break
                    else:
                        print("Invalid move. Please choose an existing tower and a valid new height.")
                except ValueError:
                    print("Please enter valid integer values for the tower number and height.")
                except IndexError:
                    print("Please choose a valid tower number.")
        else:
            print("P2's turn:")
            move_made = False
            for index, height in enumerate(towers):
                if height > 1:
                    print(f"P2 reduces Tower {index + 1} from height {height} to 1.")
                    towers[index] = 1
                    move_made = True
                    break

            if not move_made:
                print("P2 has no move and loses.")
                return "P1"  # If P2 has no move, P1 wins

        # Switch turns
        p1_turn = not p1_turn

# Start the game
if __name__ == "__main__":
    n = int(input("Enter the number of towers: "))
    m = int(input("Enter the initial height of the towers: "))
    winner = tower_breakers(n, m)
    print(f"The winner is: {winner}")

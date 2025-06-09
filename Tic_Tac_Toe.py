import time

# ASCII art for the game title
ttt = """⟦T⟧⟦i⟧⟦c⟧ ⟦T⟧⟦a⟧⟦c⟧ ⟦T⟧⟦o⟧⟦e⟧"""

class TicTacToe:
    # Constructor method for the TicTacToe class
    # Corrected: __init__ needs two underscores on each side
    def __init__(self):
        # Initialize the board as a list of 9 empty spaces
        self.board = [' '] * 9
        # Set the starting player to 'X'
        self.current_player = 'X'

    # Method to display the current state of the board
    def display_board(self):
        print(f"\n\n --------------- {ttt} ----------------\n\n")
        # Print the board rows with separators
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    # Method to get the player's move
    def get_player_move(self):
        while True:
            try:
                # Prompt the current player to choose a position (1-9)
                position = int(input(f"\n{self.current_player}'s turn. Choose a position (1-9): "))
                # Check if the chosen position is within the valid range and is currently empty
                if 1 <= position <= 9 and self.board[position - 1] == ' ':
                    return position
                else:
                    print("Invalid move. Please choose a valid and empty position.")
            except ValueError:
                # Handle cases where the input is not a number
                print("Invalid input. Please enter a number.")

    # Method to make a move on the board
    def make_move(self, position):
        # Place the current player's mark on the chosen position
        self.board[position - 1] = self.current_player

    # Method to switch players
    def switch_player(self):
        # If current player is 'X', switch to 'O', otherwise switch to 'X'
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Method to check if there's a winner
    def check_winner(self):
        # Define all possible winning combinations (rows, columns, diagonals)
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        # Iterate through each winning combination
        for combo in winning_combinations:
            a, b, c = combo
            # Check if all three positions in the combination are the same player's mark and not empty
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True  # A winner is found
        return False  # No winner yet

    # Method to check if the game is a tie
    def is_tie(self):
        # If there are no empty spaces left on the board and no winner, it's a tie
        return ' ' not in self.board

    # Main method to play the Tic-Tac-Toe game
    def play(self):
        while True:
            self.display_board()  # Show the current board
            position = self.get_player_move()  # Get valid move from current player
            self.make_move(position)  # Apply the move to the board

            if self.check_winner():
                self.display_board()  # Display final board with win
                print(f"\nPlayer {self.current_player} wins!\n")
                time.sleep(2)  # Pause for a moment to see the win
                break  # End the game
            elif self.is_tie():
                self.display_board()  # Display final board with tie
                print("\nThe game is a tie!\n")
                time.sleep(2)  # Pause for a moment to see the tie
                break  # End the game
            
            self.switch_player()  
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
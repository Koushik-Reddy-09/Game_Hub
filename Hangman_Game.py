import random

hg = """⟦H⟧⟦A⟧⟦N⟧⟦G⟧⟦M⟧⟦A⟧⟦N⟧ ⟦G⟧⟦A⟧⟦M⟧⟦E⟧"""

class HangmanGame:
    hangman_stages = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''']

    word_list = [
        "apple", "banana", "castle", "dancer", "elephant",
        "flame", "grapes", "honest", "island", "jungle",
        "kettle", "lemon", "mango", "novel", "ocean",
        "piano", "quilt", "rocket", "sunny", "tiger",
        "umbra", "vivid", "window", "microphone", "yellow",
        "zebra", "across", "badge", "cloud", "donkey",
        "eagle", "fairy", "garden", "humble", "jolly",
        "kitten", "leash", "birth", "nature", "ostrich",
        "peach", "rabbit", "sunset", "table", "umbrella",
        "wisdom", "whale", "phone", "comet", "dolphin",
        "direction", "naughty", "order", "pillow", "quiet",
        "roast", "important", "object", "bottle", "yeast",
        "giraffe", "suraj", "kaushik", "yashwanth", "krish", "ram"
    ]

    def __init__(self):
        pass

    def choose_word(self):
        return random.choice(self.word_list)

    def display_word(self, word, guessed_letters):
        return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

    def play(self):
        while True:
            print(f"\n\n\t\t   ----------{hg} ----------")
            print("\n\n 𝓕𝓲𝓷𝓭 𝓽𝓱𝓮 𝓰𝓲𝓿𝓮𝓷 𝔀𝓸𝓻𝓭 :")
            lives = 0
            chosen_word = self.choose_word()
            guessed_letters = set()

            print('\n\n', self.display_word(chosen_word, guessed_letters))

            game_over = False
            while not game_over:
                guess_letter = input("\n\n Guess a letter: ").lower()

                if not guess_letter.isalpha() or len(guess_letter) != 1:
                    print("Please enter a single valid letter.")
                    continue

                if guess_letter in guessed_letters:
                    print("You've already guessed that letter.")
                    continue

                guessed_letters.add(guess_letter)

                if guess_letter not in chosen_word:
                    lives += 1
                    print(self.hangman_stages[lives])
                    if lives == 6:
                        game_over = True
                        print("\n\n SORRY... YOU LOSE!")
                else:
                    print("Good guess!")

                display = list(self.display_word(chosen_word, guessed_letters))
                print('\n', ' '.join(display))

                if '_' not in display:
                    game_over = True
                    print("\n\n CONGRATS... YOU WON!")

            print(f"\n\n The word was '{chosen_word}'")
            play_again = input("\n\n Do you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                print("\n Thank you for playing! I hope you enjoyed the game.")
                break

# Start the game
if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.play()
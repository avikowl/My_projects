import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_ending = False
lives = 8
display = []
for _ in range(word_length):
    display += "_"

while not game_ending:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"It's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_ending = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_ending = True
        print("You win.")
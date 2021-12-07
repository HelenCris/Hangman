import random
from hangman_words import word_list
chosen_word = random.choice(word_list)


word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

print(stages[6])


display = []

for letter in chosen_word:
    display.append("-")
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        
        lives -= 1 
        if lives == 0: 
            print(stages[lives])
            print("You lose")
            break
        else:
            print(stages[lives])
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(f"{' '.join(display)}")

    if "-" not in display:
        end_of_game = True
        print("You win.")



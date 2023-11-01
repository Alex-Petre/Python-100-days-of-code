import random
import hangman_art
import hangman_words


def generate_random_word():
    word = random.choice(hangman_words.word_list)
    return word

chosen_word = generate_random_word()
print(hangman_art.logo)

word_length = len(chosen_word)

display = []
for i in range(word_length):
    display += "_"

print(f"{''.join(display)}\n")


lives = 6
game_over = False
while not game_over:
    guess = input("Ghicește o literă: ").lower()

    for position in range(word_length):
        char = chosen_word[position]
        if char == guess:
            display[position] = char

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\nAi pierdut.")
            print(f"\nCuvantul era: {chosen_word}")

    print(f"{''.join(display)}")

    if "_" not in display:
        game_over = True
        print("\nAi câștigat.")

    print(hangman_art.HANGMANPICS[lives])
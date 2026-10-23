
import random

words = ["python", "robot", "rocket", "sensor", "drone"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:
    # Display the word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    # Check if the player won
    if "_" not in display:
        print("Congratulations! You won!")
        break

    # Get the player's guess
    guess = input("Enter one letter: ").strip().lower()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

else:
    print("\nGame over! You ran out of attempts.")

print("The secret word was:", secret_word)

play_again = input("Play again? (yes/no): ").strip().lower()
if play_again == "yes":
    print("Run the program again to play another round.")
else:
    print("Thanks for playing!")

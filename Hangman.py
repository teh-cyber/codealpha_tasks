import random

words = ["python", "computer", "programming", "keyboard", "software"]

secret = random.choice(words)

attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0:

    print("\nWord:", end=" ")

    for letter in secret:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print(f"\nAttempts left: {attempts}")

    g = input("Guess a letter: ").lower()

    if len(g) != 1 or not g.isalpha():
        print("Please enter one letter only.")
        continue

    if g in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(g)

    if g in secret:
        print("Correct!")
    else:
        print("Wrong!")
        attempts -= 1

    won = True

    for letter in secret:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print("\nCongratulations! You guessed the word!")
        print("The word was:", secret)
        break

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", secret)
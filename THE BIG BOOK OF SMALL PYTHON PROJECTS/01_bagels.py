"""Bagels, by Al Sweigart al@inventwithpython.com
  2. A deductive logic game where you must guess a number based on clues.
  3. This code is available at https://nostarch.com/big-book-small-python-programming
  4. A version of this game is featured in the book, "Invent Your Own
  5. Computer Games with Python" https://nostarch.com/inventwithpython
  6. Tags: short, game, puzzle"""

import random



num_digits = 3
max_guesses = 10

def main():
    print(
        '''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct. 
    For example, if the secret number was 248 and your guess was 843, 
    the clues would be Fermi Pico.'''.format(num_digits))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_number = get_secret_number()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != num_guesses or not guess.isdecimal():
                print("Guess #{}:".format(num_guesses))
                guess = input("> ")

                clues = getClues(guess, secret_number)
                print(clues)
                num_guesses += 1

                if guess == secret_number:
                    break  # They're correct, so break out of this loop.
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print('The secret number was {}.'.format(secret_number))
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def get_secret_number():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('1234567890')  # creating a list of the digits used constructing the secret number
    random.shuffle(numbers)  # shuffle them in to a random order

    # get the first number of digits from the shuffeled list
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return f"YOU WIN!!! The secret num is {secret_num}!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:  # # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secret_num[i]:  # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return "Bagels"
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()



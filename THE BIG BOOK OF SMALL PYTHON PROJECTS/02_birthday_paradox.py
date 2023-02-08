"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
  2. Explore the surprising probabilities of the "Birthday Paradox".
  3. More info at https://en.wikipedia.org/wiki/Birthday_problem
  4. This code is available at https://nostarch.com/big-book-small-python-programming
  5. Tags: short, math, simulation"""

import datetime
import random


def getbirthdays(numberOfbirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []

    for j in range(numberOfbirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a


# intro of the program
print(
    '''Birthday Paradox, by Al Sweigart al@inventwithpython.com
The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
'''
)

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:

    responce = input('How many birthdays shall I generate? (Max 100): ')
    if responce.isdecimal() and 0 < int(responce) <= 100:
        number_of_birthdays = int(responce)
        break
print()
print('Here are', number_of_birthdays, 'birthdays:')
birthdays = getbirthdays(number_of_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")
    month_name = months[birthday.month - 1]
    dateText = '{} {}'.format(month_name, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    month_name = months[match.month - 1]
    dateText = '{} {}'.format(month_name, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', number_of_birthdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = getbirthdays(number_of_birthdays)
    if getMatch(birthdays) != None:
        sim_match += 1
print('100,000 simulations run.')

# displaying the results
probability = round(sim_match / 100000 * 100, 2)
print('Out of 100,000 simulations of', number_of_birthdays, 'people, there was a')
print('matching birthday in that group', sim_match, 'times. This means')
print('that', number_of_birthdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

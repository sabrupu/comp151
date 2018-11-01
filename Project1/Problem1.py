# Problem 1: Blackjack

import random


playing_count = 0


def roll_die():
    return random.randint(1, 6)


def hit():
    playing_count = roll_die() * 2
    print('Hit!')
    print('\tRolling dice...')
    die1 = roll_die()
    die2 = roll_die()
    both = die1 + die2
    print(f'\t\t1. Die #1    = {die1}.')
    print(f'\t\t2. Die #2    = {die2}.')
    if playing_count + both > 21:
        num_choices = 2
    else:
        print(f'\t\t3. Both dice = {both}.')
        num_choices = 3
    choice = 0  # Force while condition to avoid repeated code
    while choice not in range(1, num_choices+1):
        choice = int(input('Choose one of the above options: '))
    global playing_count  # We are able to access this variable everywhere in this code
    if choice == 1:
        playing_count += die1
    elif choice == 2:
        playing_count += die2
    else:
        playing_count += both


def main():
    return


main()

# Problem 1: Blackjack

import random


def roll_die():
    return random.randint(1, 6)


def deal():
    print('Deal!')
    print('\tRolling dice...')
    die1 = roll_die()
    die2 = roll_die()
    print(f'\t\tDie #1  =  {die1}')
    print(f'\t\tDie #2  =  {die2}')
    playing_count = (die1 + die2) * 2
    return playing_count


def hit(playing_count):
    print('Hit!')
    print('\tRolling dice...')
    die1 = roll_die()
    die2 = roll_die()
    both = die1 + die2
    print(f'\t\t1. Die #1  =  {die1}')
    print(f'\t\t2. Die #2  =  {die2}')
    if playing_count + both > 21:
        num_choices = 2
    else:
        print(f'\t\t3. Both    =  {both}')
        num_choices = 3
    choice = 0  # Force while condition to avoid repeated code
    while choice not in range(1, num_choices+1):
        choice = int(input('\tChoose one of the above options: '))
    if choice == 1:
        playing_count += die1
    elif choice == 2:
        playing_count += die2
    else:
        playing_count += both
    return playing_count


def main():
    print('Blackjack\n')
    playing_count = deal()
    print(f'Initial playing count = {playing_count}\n')

    hit_or_stand = input('Type "hit" or "stand": ')
    while hit_or_stand == 'hit':
        playing_count = hit(playing_count)
        print(f'Playing count = {playing_count}\n')
        hit_or_stand = input('Type "hit" or "stand": ')


main()

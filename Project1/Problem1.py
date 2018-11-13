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


def play_as_player():
    # Deal
    playing_count = deal()

    # Loop until player stands or busts
    while True:
        # Show playing count
        print(f'\n\tPlaying count = {playing_count}\n')

        # Check for bust
        if playing_count > 21:
            print('Bust!')
            return playing_count

        # Hit or stand
        hit_or_stand = input('Hit or Stand: ')
        if hit_or_stand == 'hit':
            playing_count = hit(playing_count)
        else:
            print('Stand!')
            return playing_count


def play_as_dealer(playing_count_player):
    # Deal
    playing_count = deal()

    # Loop until dealer stands or busts
    while True:
        # Show playing count
        print(f'\n\tPlaying count = {playing_count}\n')

        # Check for bust
        if playing_count > 21:
            print('Bust!')
            return playing_count

        # Hit or stand
        if playing_count <= playing_count_player and playing_count <= 17:
            print('Hit!')
            print('\tRolling die...')
            die = roll_die()
            print(f'Die  =  {die}')
            playing_count += die
        else:
            print('Stand!')
            return playing_count


def main():
    print('Blackjack\n')
    playing_count_player = play_as_player()
    playing_count_dealer = play_as_dealer(playing_count_player)


main()

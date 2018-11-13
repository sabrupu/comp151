# Problem 1: Blackjack

import random


def roll_die():
    return random.randint(1, 6)


def deal():
    print('\nDeal!')
    print('\tRolling dice...')
    die1 = roll_die()
    die2 = roll_die()
    print(f'\t\tDie #1  =  {die1}')
    print(f'\t\tDie #2  =  {die2}')
    playing_count = (die1 + die2) * 2
    return playing_count


def hit(playing_count):
    print('\nHit!')
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


def get_hit_or_stand():
    choice = ''
    while choice not in ['hit', 'stand']:
        choice = input('\nHit or Stand: ').lower()
    return choice


def play_as_player():
    # Deal
    playing_count = deal()

    # Loop until player stands or busts
    while True:
        # Show playing count
        print(f'\n\tPlaying count = {playing_count}')

        # Check for bust
        if playing_count > 21:
            print('\nBust!')
            return playing_count

        # Hit or stand
        choice = get_hit_or_stand()
        if choice == 'hit':
            playing_count = hit(playing_count)
        else:
            print('\nStand!')
            return playing_count


def play_as_dealer(playing_count_player):
    # Deal
    playing_count = deal()

    # Loop until dealer stands or busts
    while True:
        # Show playing count
        print(f'\n\tPlaying count = {playing_count}')

        # Check for bust
        if playing_count > 21:
            print('\nBust!')
            return playing_count

        # Hit or stand
        if playing_count <= playing_count_player and playing_count <= 17:
            print('\nHit!')
            print('\tRolling die...')
            die = roll_die()
            print(f'\t\tDie  =  {die}')
            playing_count += die
        else:
            print('\nStand!')
            return playing_count


def main():
    print('Blackjack')

    # Player's turn
    playing_count_player = play_as_player()

    if playing_count_player > 21:
        result = 'Dealer wins!'
    else:
        # Dealer's turn
        playing_count_dealer = play_as_dealer(playing_count_player)

        if playing_count_dealer > 21:
            result = 'Player wins!'
        elif playing_count_dealer < playing_count_player:
            result = 'Player wins!'
        elif playing_count_dealer > playing_count_player:
            result = 'Dealer wins!'
        else:
            result = 'Tie!'

    print(f'\n{result}')


main()

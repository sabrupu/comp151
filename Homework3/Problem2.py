# Write a program that will play a game of Tic-Tac-Toe.
# Read player moves as coordinates (1 1 would be the center square).
# Store the board as a 2D list.
# Here is the board with the coordinates of each move.
#               [0, 0] [0, 1] [0, 2]
#               [1, 0] [1, 1] [1, 2]
#               [2, 0] [2, 1] [2, 2]


board = [[' '] * 3 for _ in range(3)]  # create 3 separate lists of 3 elements


def print_board():
    print()
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('---+---+---')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('---+---+---')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()


def get_coords():
    # Loop until the coordinates are valid and not already taken
    while True:
        coords = input('Enter coordinates: ').split(' ')

        # Only proceed if there are exactly two coordinates
        if len(coords) == 2 and coords[0].isdigit() and coords[1].isdigit():
            row = int(coords[0])
            col = int(coords[1])

            # Check that the coordinates are on the board
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return [row, col]


def is_winner(player):
    # Check rows for winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Check columns for winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

    return False


def main():
    print('Game of Tic-Tac-Toe\n')

    print_board()

    turns = 0
    keep_playing = True
    while keep_playing:
        for player in 'XO':
            print(f'{player}\'s turn')
            [row, col] = get_coords()
            board[row][col] = player
            print_board()

            if is_winner(player):
                print(f'{player} won!')
                keep_playing = False
                break

            turns += 1
            if turns == 9:
                print('Draw!')
                keep_playing = False
                break


main()

# Write a program that will play a game of Tic-Tac-Toe.
# Read player moves as coordinates (1 1 would be the center square).
# Store the board as a 2D list.
# Here is the board with the coordinates of each move.
#               [0, 0] [0, 1] [0, 2]
#               [1, 0] [1, 1] [1, 2]
#               [2, 0] [2, 1] [2, 2]


board = [[' '] * 3 for _ in range(3)]  # create 3 separate lists of 3 elements


def print_board():
    for row in board:
        for space in row:
            print(space, end=' ')
        print()


def get_coords():
    # Loop until the coordinates are valid and not already taken
    while True:
        coords = input('Enter coordinates: ').split(' ')

        if len(coords) == 2:
            row = int(coords[0])
            col = int(coords[1])

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


main()

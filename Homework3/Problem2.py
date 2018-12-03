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


def check_winner(player_sym):
    pass


def main():
    print('Game of Tic-Tac-Toe\n')

    print_board()

    keep_playing = True

    while keep_playing:
        for sym in 'XO':
            print(f'{sym}\'s turn')
            [row, col] = get_coords()
            board[row][col] = sym
            print_board()


main()

# You will write a python program which will do the following things:
# 1. Ask the user for a number of game results n.
# 2. Prompt the user for all n game results (the user will enter 1 for a win or 0 for a
# loss)
# 3. Keep a running total of the number of victories
# 4. After all of the results are submitted, find the win percentage
# 5. Report that win percentage to the user
# Ensure that the user only enters either a 1 or a 0! If any other value is entered, re-prompt
# without counting it.


# Enter number of game results
n = int(input('Enter number of game results: '))

# Enter game results
victories = 0  # running total of the number of victories
for i in range(n):
    game_result = int(input(f'Game result {i+1}: '))
    while game_result != 1 and game_result != 0:
        print('Invalid game result. Enter 1 for a win or 0 for a loss.')
        game_result = int(input(f'Game result {i+1}: '))
    victories += game_result


# Calculate and print win percentage
win_percentage = victories / n
print(f'\nWin percentage: {win_percentage:.2%}\n')

# You will build a "Fortune cookie" program. For those of you not familiar with it, once
# upon a time there was a command line program for power users which would give a
# random saying printed on the command line.
#
# In your program you will
#     ● Create a text file in your project folder with at least 20 "quirky sayings"/fortunes
#       (the only requirement is that they be appropriate for display in class),
#     ● Create a list by reading those 20 fortunes from your file
#     ● Ask the user how many fortunes he/she wants to see.
#         ○ store the value in a variable
#     ● Inside of a loop (loop as many times as the user asked)
#       ● select a random answer from your list of fortunes
#       ● wait for the user to press the enter key (the easy way is to use the input
#          method)
#
# Note that it is quite possible that you will see some fortunes more than once while not
# seeing some at all.

# Each word is the key, its value is the count
# {"the" : 0, "and" : 0}
# if entry["number"] = search for value
# convert everything to lower as well as the user input

import random

# Read fortune list from file
file = open('Fortunes.txt', 'r')
fortunes = file.readlines()
file.close()

# Ask user how many fortunes he/she would like to see
num_fortunes = int(input("How many fortunes would you like to see? "))

# Print random fortunes
for i in range(num_fortunes):
    r = random.randrange(0, len(fortunes))
    input()
    print(fortunes[r])

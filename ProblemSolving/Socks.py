#                2. hands       Table
# Lower bound       2             2
# Upper bound    infinite         4

#   Red Blue Green
#   RR    RB  RG
#   BB    BR  BG
#   GG    GB  GR

# Import the randint() function from the 'random' library
from random import randint


def main():
    # number of times to simulate each algorithm
    epochs = 1000000

    # Stores the average cost of each algorithm across 'epoch' iterations
    two_hands_method_efficiency = test_efficiency(socks_two_hands, epochs)
    table_method_efficiency = test_efficiency(socks_with_table, epochs)

    # Displays a single run of each algorithm to the user
    print(f"Two-hands method: {socks_two_hands()}")
    print(f"Table method:     {socks_with_table()}")
    print()
    # Displays the average of 'epoch' iterations to the user
    print(f"Two-hands method: {two_hands_method_efficiency}")
    print(f"Table method:     {table_method_efficiency}")
    print()
    # Displays the % increase of the table method over the 2-hand method
    print(f"Over {epochs} runs, calculated an average of a {abs(table_method_efficiency - two_hands_method_efficiency) / table_method_efficiency * 100:.2f}% increase")


# Strategy to get a matching pair by drawing two socks and putting them back
# until we draw a matching pair.
def socks_two_hands():
    # Draw our first 2 socks and start our counter at 2
    sock1 = randint(1, 3)
    sock2 = randint(1, 3)
    counter = 2

    # Continue to draw socks & increment our counter
    # until we have a matching pair
    while(sock1 != sock2):
        sock1 = randint(1, 3)
        sock2 = randint(1, 3)
        counter += 2

    return counter

# Strategy to get a matching pair by drawing a sock and putting it on
# our table until we have a matching pair.


def socks_with_table():
    # Create my "table" (an empty list) and start my counter at 2
    sock_list = []
    counter = 2

    # Draw two socks and place them on my table (at the end of my list)
    sock_list.append(randint(1, 3))
    sock_list.append(randint(1, 3))

    # Until we end up with exactly 2 of any type of sock (1, 2, or 3) then continue
    # to loop
    while(sock_list.count(1) != 2 and sock_list.count(2) != 2 and sock_list.count(3) != 2):
        # Add another sock to our table
        sock_list.append(randint(1, 3))
        # Increment our counter by 1
        counter += 1

    return counter

# This function will accept a function & a number of times to run said function


def test_efficiency(fun, epochs):
    sum = 0

    # This will run a number of times equal to "epochs"
    for i in range(epochs):
        # Execute the function given and add the result to "sum"
        sum += fun()

    # Calculate & return the average # of socks drawn across all simulations
    return sum / epochs


main()

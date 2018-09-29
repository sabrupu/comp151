def my_function() :
    print('Hello, ')
    print('World!')
    return 'Done'

print('Outside function!')
my_var = my_function()
print(my_var)


def add(a, b):
    return a + b
def sub(a, b):
    return a - b

sum     = add(50, 10)
diff    = sub(50, 10)

print(sum / diff)
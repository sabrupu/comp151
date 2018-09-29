def main():
    user_name = get_user_name()
    greet_user(user_name)
    return
# 5. greet_user_name gets executed
# 2. get_user_name gets executed

def get_user_name():
    name = input('What is your name?')
    return name
# 3. name gets executed
# 4. return name gets executed

def greet_user(user_name):
    print(f'Hello {user_name}, nice to meet you!');



main()
# 1. invoke the main function, this gets executed first





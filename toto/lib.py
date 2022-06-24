from termcolor import colored

def whats_my_name():

    return "My name is Daniel"

def who_am_i():

    name = whats_my_name()

    # cannot be tested since the function returns None implicitly
    print(colored(name, "blue"))

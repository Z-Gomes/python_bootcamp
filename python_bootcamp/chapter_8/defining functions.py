# a function is a block of code designed to do a specific job
# use def at beginning of function to store a block of code to 'call' later

def greet_user():
    """Display a simple greeting message."""
    # """ triple quotations contain docstrings, which describe the purpose of a function, and python searches for these """
    print('Hello!')
    
greet_user()

# you can pass information into a function inside its () by defining what is inside the ()

def greet_user(username):
    """Display a simple greeting message, including a name"""
    print(f"Hello, {username.title()}, how are you?")

greet_user('jesse')

# each time you call the function greet_user, python expects you will input some value for username each time


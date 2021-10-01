# input() pauses your program and waits for the user to enter information
# after the user enters info, python ties it to a variable to continue working with it

message = input("Tell me something and I will repeat it back to you: ")
print(message)

# the text inside input() is shown to the user, then after they enter something, it prints that as message

name = input("Please type your full name: ")
print(f'\nHello, {name}')

# if you want to write a multi-line prompt, assign it to a variable and use that as your input message

prompt = 'If you tell us your first and last name, we can personalize what you see'
prompt += '\nWhat is your first name?: '

Name = input(prompt)
print(f'Hello, {Name}!')

# input() only accepts values entered by the user as string formats
# the int() function converts your input() string to an integer

age = input('How old are you: ')
age = int(age)
age >= 18

# input tool using int() to determine what shoe size to wear at your store

shoe_size = input("Please enter your normal shoe size: ")
shoe_size = int(shoe_size)

if shoe_size > 10:
    print('Your suggested shoe size is Large')
elif shoe_size > 4 and shoe_size <= 10:
    print('Your suggested shoe size is Medium')
else:
    print('Your suggseted shoe size is Small')

# modulo operator % will divide numbers and offer the remainder

4%2
7%2
121%2

number = input('Type any number here: ')
number = int(number)

if number % 2 == 0:
    print('the number is even')
else:
    print('the number is odd')


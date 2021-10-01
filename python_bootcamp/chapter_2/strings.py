name = 'ada lovelace'
print(name.title())

##anything inside single quotes is considered a string in python; you can also use double quotes around a string

##the METHOD "title" here appears after the variable in the print() call
# METHOD is an action that python can perform on a piece of data
# every method is followed by a set of parentheses because they usually need more info to do their work
# title() does not need any additional info, so we can leave parentheses empty in this example

print(name.upper())
print(name.lower())

## upper() method prints in all caps, lower() in all lower case
# lower() method is often useful to name things, since names must be all lower case

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

## F-STRINGS where the f is placed before "" and brackets around names of variables inserts variables into strings

message = f'Hello, {full_name.title()}'
print(message)

## to add a tab of whitespace into strings, use \t 
# to add a new line of whitespace, use \n
# tabs and new lines can be combined into a single string with \n\t combinations

print("Languages:\n\tPython\n\tJavascript\n\tC++")

##removing whitespace
#python considers whitespace important unless you tell it otherwise
#rstrip() method ensures that no whitespace exists at the right end of a string

favorite_language = 'Python '
print(favorite_language)
favorite_language.rstrip()
favorite_language

##string syntax errors with quote marks inside strings
# setting up a string with double quotes enables python to read the single quotes inside it correctly
# if you set it up with single quotes, python can't interpret where the string ends

# message = 'One of Python's strengths is its diverse community.
#returns an error

message = "One of Python's strengths is its diverse community."
print(message)

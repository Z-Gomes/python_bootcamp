# the simplest if statements contain a condition and then an action to follow on the condition

age = 10
if age >= 18:
    print('Congratulations, you are eligible to drink liquor in Europe')

# you can have as many lines of code as you want in the block following the if statement
# when the conditional test passes, both lines of code in the block follwing if are executed

if age < 18:
    print("I'm sorry, you're not old enough to drink liquor here yet")
    print('Would you like a fanta instead?')

# if else statements offer a way to take action if certain values pass and others fail

age = 16
if age >= 18:
    print("Congratulations, you're old enough to drink liquor in Europe")
    print("Would you like to order a drink?")
else:
    print("Sorry, you are too young to drink liquor here")
    print("Why don't you try a nice cup of fanta?")

# python runs an if-elif-else block if multiple tests are required
# python will run each test in sequence until one of the conditions passes

age = 12
if age < 4:
    print("You're ticket is free")
elif age  < 65:
    print("You're ticket is full price")
else:
    print("You're ticket is Senior price")

# inserting variables into elif statements allows for flexible outputs



age = 12
if age < 4:
    price = 'Free'
elif age < 18:
    price = 20
else: 
    price = 15

print(f'Your ticket price today will be {price}')

# you may use as many elif blocks as you like as part of your if statement
# if you omit the else at the end of your statement, every block of code will require a pass to execute, but it will still function


# range() function allows you to generate a series of numbers via loops

for value in range(1,5):
    print(value)

# in this example, range() only prints numbers 1-4, not 5
# range always starts at the first value you provide and stops (not includes) at the last value

#to print values 1-5, you'd need to make a range til 6

for value in range(1,6):
    print(value)

# use the list() function wrapped around the range() function to create a list of numbers

numbers = list(range(1,6))
print(numbers)

# you can skip numbers in a list by passing a third argument into the range() function, that value is the step size for generating numbers

even_numbers = list(range(2,11,2))
print(even_numbers)

# you can create nearly any list using range()

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# or make this cleaner with

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# you can find min, max, and sum a list of numbers with min() max() and sum()

digits = list(range(1,9))
digits
min(digits)
max(digits)
sum(digits)

# list comprehensions generate lists in single lines of code by combining for loops and creation of new elements into a single line
# inside the list brackets, first define the expression for the values to be stored in the list
# then, write a for loop to generate the numbers from the expression to be fed to the list, close the brackets

squares = [value**2 for value in range(1,11)]
print(squares)

#just for fun

test = list(range(1,21))
for number in test:
    print(number)

mil = list(range(1,1_000_001))
sum(mil)
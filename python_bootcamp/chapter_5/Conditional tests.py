cars =  ['audi', 'bmw', 'toyota', 'suburu']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for equality is done using double ==
# single = means assigning values to a variable

car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'

# case matters when checking true/false conditions, but you can convert variable values to lowercase before checking if you want

car = 'Audi'
car == 'audi'

car.lower() == 'audi'

# using the != command will check if two values are not equal

car = 'Audi'
car != 'audi'

car.lower() != 'audi'

requested_topping = 'pineapple'
if requested_topping == 'pineapple':
    print('Pinapples on pizza is an insult to pizza.\nNo thank you')

# you can conduct mathematical checks of various types
# including: equals, less than, greater than, etc

answer = 17
answer != 42

age = 19
age > 19
age <20
age <= 19
age >= 25

# use keyword and to test if multiple conditions are true at the same time

age_0 = 22
age_1 = 19

age_0 > 10 and age_1 <100

# the keyword or allows you to check multiple conditions if any one of them are true

age_0 == 20 or age_1 < 50
age_0 == 20 or age_1 == 500

# use keyword in to find out if a value is already within a list somewhere

requested_toppings = ['pepperoni', 'mushroom', 'sausage', 'pineapple']
'mushroom' in requested_toppings
'peppers' in requested_toppings

# use keyword not in combination with in to see if an item is not already in a list

'pepperoni' not in requested_toppings
'basil' not in requested_toppings

zachs_topping = 'pepperoni'
if zachs_topping in requested_toppings:
    print(f'Yes, Zach, we have {zachs_topping} as an available topping')

zachs_topping = 'barbecue chicken'
if zachs_topping not in requested_toppings:
    print(f"I'm sorry Zach, but {zachs_topping} is not available as a topping")


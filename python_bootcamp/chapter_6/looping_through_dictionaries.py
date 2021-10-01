# new dictionary for use in this file

user_0 = {
    'username':'zgomes@indigoag.com',
    'first':'zach',
    'last':'gomes'
}

# you can loop through a dictionary if you want to see everything stored in it
# the method items() returns a list of key-value pairs

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

# new dictionary to demonstrate

favorite_foods = {
    'basement josh':'pizza',
    'upstairs josh':'guacamole',
    'xiaowei':'barbecue',
    'jyoti':'chitlins',
    'zach':'dumplings'
}

for name,food in favorite_foods.items():
    print(f"{name.title()}'s favorite food is {food}.")

# keys() method is useful when you don't need to work with all values in a dictionary, only the keys

for name in favorite_foods.keys():
    print(name.title())

# looping through keys is default behavior in for loops through dictionaries

for name in favorite_foods:
    print(name.title())

# create a list and run a loop with a condition through the dictionary using the list

friends = ['basement josh', 'xiaowei']
for name in favorite_foods.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        favorite_food = favorite_foods[name]
        print(f"\t{name.title()}, I see you love {favorite_food}!")


# looping through a dictionary returns items in the same order they were inserted
# the sorted() function enables you to run through the dictionary items according to alphabetical order

for name in sorted(favorite_foods.keys()):
    print(f"{name.title()}, bon appetit!")

# values() method allows you to return a list of values without any keys

print("The following foods are on the menu tonight:\n")
for favorite_food in favorite_foods.values():
    print(favorite_food.title())

# to see each value without potential repetition, use a set

for favorite_food in set(favorite_foods.values()):
    print(favorite_food.title())
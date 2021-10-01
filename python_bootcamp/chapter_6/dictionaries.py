# dictionaries are collections of key-value pairs
# each key is connected to a value, and you can use that key to access the value associated with it

# dictionaries are wrapped in {} with key-value pairs inside

alien_0 = {'color': 'green', 'points': 5}

# you can store as many key-value pairs as you want inside a dictionary

# access a value by giving the name of the dictionary and placing the key inside []

print(alien_0['color'])

# you can access any value by providing the key

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# you can add new key-value pairs to a dictionary by giving the name of the dictionary followed by the new key inside []

alien_0['x_position'] = 0
alien_0['y position'] = 25
print(alien_0)

# you can start with an empty dictionary by using blank {} and add new items to it as you go

zach = {}

zach['eye color'] = 'green'
zach['height'] = '5 ft 10 in'
zach['intelligence'] = 'meh'
zach['hair color'] = 'brown'
zach['weight'] = 170

print(zach['intelligence'])

# to modify values in a dictionary, give the dictionary name, key in [] and new value you want associated with the key

print(f"Zach's height is {zach['height']}.")

zach['height'] = '5ft 9.5in'
print(f"Zach's actual height is {zach['height']}, he rounded up.")

# see what happens to Zach when he eats

meal = 'pasta'

if meal == 'salad':
    zach_weight_change = 1
elif meal == 'chicken wings':
    zach_weight_change = 5
elif meal == 'pasta':
    zach_weight_change = 10
else:
    zach_weight_change = 0

zach['weight'] = zach['weight'] + zach_weight_change

print(f"Zach just ate {meal}, his new weight is {zach['weight']}.")

# use the del statement to remove a key-value pair from a dictionary

del zach['intelligence']
print(zach)

# format dictionaries for ease of use, such as when storing information about different objects in one dictionary

team_astrology = {
    'jyoti':'scorpio',
    'upstairs josh': 'virgo',
    'basement josh': 'leo',
    'xiaowei':'libra',
    'zach':'pisces'
}

sign = team_astrology['basement josh'].title()
print(f"Basement Josh's sign is {sign}")


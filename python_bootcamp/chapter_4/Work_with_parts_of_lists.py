# to slice a list, indicate the first and last index of the items in the list you want to work with

players = ['charles', 'chris', 'steven', 'jj', 'josh', 'zach']
print(players[0:3])

# without a starting item in the index, python starts with the first item in the list
print(players[:5])

# omitting the ending index in the list will make python read until the end of the list

print(players[2:])

#because a negative item in an index refers to an element a certain distance from the end of the list, you can count down from the end by using a negative number

print(players[-2:])

print(players[:-4])

# you can also create loops to execute through a list up until the end of the slice

print('The players in our escape room for survival game tonight will be:')
for player in players[:3]:
    print(player.title())

# you can copy a list by making a slice of a list with no start and end

my_foods = ['pizza', 'stir fry', 'salad', 'sandwich', 'hamburger', 'hot dog']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print("And my friend's favorite foods are:")
print(friend_foods)

my_foods.append('lasagna')
friend_foods.append('sausage')

print(my_foods)
print(friend_foods)


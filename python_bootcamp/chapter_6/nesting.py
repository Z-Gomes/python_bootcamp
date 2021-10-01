# you can store multiple dictionaries in a list or a list of items as a value, which is called nesting

# multiple TVG team dictionaries made into a list

TVG_1 = {'name': 'basement josh', 'game':'poker'}
TVG_2 = {'name': 'xiaowei', 'game':'slots'}
TVG_3 = {'name': 'jyoti','game': 'roulette'}

TVG_team = [TVG_1, TVG_2, TVG_3]

for person in TVG_team:
    print(person)

# creating multiple dictionaries inside the list with code to generate them automatically
# use range() to say how many new items to add

FDS_team = []

for FDS_member in range(30):
    new_member = {'name':'cyborg Jay', 'game':'baccarat'}
    FDS_team.append(new_member)

# show first 5 new team members
for new_member in FDS_team:
    print(new_member)

TVG_team.append(FDS_team)

# show how many total new team members were added
print(f"Total number of FDS team members: {len(FDS_team)}")

# put a list inside a dictionary

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','pineapple','pepperoni'],
}

print(f"You ordered a {pizza['crust']}-crust pizza\nWith the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

# you can nest a list inside a dictionary any time you want more than one value to be associated with a key

favorite_foods = {
    'basement josh':['pizza','hot dogs'],
    'upstairs josh':['guacamole','burrito'],
    'xiaowei':['barbecue','pasta'],
    'jyoti':['chitlins','bloody rare steak'],
    'zach':['dumplings','pasta']
}

for name, foods in favorite_foods.items():
    print(f"\n{name.title()}'s favorite foods are:")
    for food in foods:
        print(f"{food.title()}")


# you can nest a dictionary inside another dictionary

team = {
    'jsauder':{
        'first':'basement',
        'last':'josh',
        'location':'his basement',
    },
    'jshankar':{
        'first':'jyoti',
        'last':'shankar',
        'location':'everywhere',
    },
}

for name,info in team.items():
    print(f"\n{info['first']} {info['last']}")
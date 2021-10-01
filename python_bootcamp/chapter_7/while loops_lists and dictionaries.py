# use while loops to modify lists while we work through them

# create a list of new users for a website
# use a while loop to go through that list of users, verify their ID, then add them to a new list of verified users

# unconfirmed_users = ['sarah','mike','trevor']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f'Verifying users: {current_user.title()}')
#     confirmed_users.append(current_user)

# print(f'\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# # remove all instances of a specific value from a list using remove() method inside a while loop
# # python removes the first instance of 'cats' in the while loops, then goes back and keeps checking until there are no more 'cats' in the list

# pets = ['dogs','cats','dogs','cats','parrots','hamsters','iguanas','goldfish','ferrets']

# while 'cats' in pets:
#     pets.remove('cats')

# print(pets)

# # make a polling program to prompt for a name and response through a while loop
# # store the inputs we gather in a dictionary to tie each response to a user

responses = {}
polling_active = True

while polling_active:
    # prompt for the person's name and their individual response
    name = input("\nWhat is your name? ")
    response = input("\nWhat is your favorite food? ")

    #store response in dictionary

    responses[name] = response

    # ask if there's another person who will respond, expanding our dictionary

    repeat = input('\nIs there another person who will respond (type yes or no)' )
    if repeat == 'no':
        polling_active = False
    elif repeat == 'yes':
        continue
    else:
        print('I assume you meant to indicate another person would like to respond')

# polling is completed

print("\n---Polling is complete---")
for name, response in responses.items():
   print(f"{name.title()}'s favorite food is {response}.")





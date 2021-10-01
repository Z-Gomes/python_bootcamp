# # while loops keep running as long as a condition remains true

# # loop to count up through numbers until reaching 10

# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# # += operator is short for current_number = current_number + whatever you write afterwards

# prompt = "\nTell me something, and I will repeat it back"
# prompt += "\nEnter 'quit' to end the program: "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# # use a flag to check if many statements are true simultaneously and simply

# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # break statement controls which parts of code are executed or not
# # loops that start with while True will run forever, until reaching a break statement

# prompt = "\nPlease enter the name of a city you've visited\nType 'quit' to stop the program: "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else: 
#         print(f"I've already been to {city.title()}, you provincial.")

# # the continue statement can return to the beginning of a loop based on a conditional test

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    else: 
        print(number)

# if a loop is accidentally set to run forever, ctrl + c should close the program, or simply exit the editor

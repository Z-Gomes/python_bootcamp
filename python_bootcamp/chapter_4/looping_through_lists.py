# looping allows you to take the same set of actions with every item in a list
# for loops allows python to avoid problems of retyping actions on each name in a list or reacting to list changes

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# for tells python to create the variable magician and associate the first item from magicians with that variable
# then python reads the print() line, and executes the print() command, displaying the first item in the magicians list
# but because there are more items in the magicians list, python continues to read the for command and execute the print() commmand
# after doing the last item in the list, there are no more items for python to print, so it stops

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} made a poor career choice, by becoming a magician")

# every indented line following the for command is considered 'inside the loop' - each line inside the loop is completed once for each item in the list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} made a poor career choice, by becoming a magician")
    print(f"Are you sure you don't want to apply for an accounting job, {magician.title()}?")

# any lines of code included after the for loop are only executed once

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} made a poor career choice, by becoming a magician")
    print(f"Are you sure you don't want to apply for an accounting job, {magician.title()}?")

print(f"Thanks, everyone. Glad to hear you've changed your minds.")


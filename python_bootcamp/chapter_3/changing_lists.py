#Lists can be modified up and down. To change an element, refer to the element in the list and tell python what you want the new value to be

motorcyles = ['honda', 'suzuki', 'yamaha']
motorcyles

motorcyles[0] = 'ducati'

#this changes the 'honda' to become 'ducati' because it is in position 0

#you can add elements to a list by using the append() method

motorcyles.append('honda')
motorcyles

motorcyles.append('bmw')
motorcyles

#you can add any new items into the middle of a list using the insert() method and specifying the index of the new element and the value of the new item

motorcyles.insert(0,'ducati')
motorcyles

#you can remove an item from a list using the del statement, if you know the index of the item you want to remove

del motorcyles[0]
motorcyles

#the pop() method allows you to remove the last item in a list but still work with that item after removing it
#an example of use of pop() would be when you want to get the x and y position of a target that was shot down and removed from your list, and you want to add an explosion there

motorcyles = ['honda','ducati','bmw']

popped_motorcyles=motorcyles.pop() 
motorcyles

print(f"the last motorcyle I owned was a {popped_motorcyles.title()}.")

#you can use pop() to remove any item from any position in the list by using its index inside the parentheses

motorcyles=['honda','suzuki','bmw']
popped_motorcyles = motorcyles.pop(0)
popped_motorcyles

# deciding between the del statement and pop() is based on whether you don't need to use that deleted item for anything, then use del; if you need it or data tied to it, use pop()

#if you don't know the index of the item you want to remove from your list, but do know what it's called, you can remove with the remove() method

motorcyles=['honda','ducati','suzuki','bmw']
motorcyles.remove('ducati')
motorcyles

#you can also use remove() to work with a value or variable that's being removed from a list

motorcyles=['honda','ducati','suzuki','bmw']

too_expensive = 'ducati'
motorcyles.remove(too_expensive)
motorcyles
#lists are not always created in a predictable order, that's just often how it happens
#to sort a list by alphabetical order, use the sort() method 

cars = ['bmw','audi','toyota','subaru']
cars.sort() 
cars

#you can sort in reverse order by using the sort(reverse=TRUE) condition in the method

cars.sort(reverse=True)
cars

# sorted() allows you to maintain the original order of your list but present it in a sorted fashion

cars
sorted(cars)

#you can also sort in reverse order while retaining the original list order using sorted(reverse)

#to print a list in reverse order, you can use the reverse() method, this permanently reverses the order of the list
#reverse() does not reverse print alphabetically, just the reverse order of the original list

cars.reverse()
cars

# len() will help you find the length of the list

len(cars)


# Tuples create lists of items that cannot change

# Tuples are like lists, but you use () instead of []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# you can't change the values for a tuple, you'll get an error if you try

dimensions[0] = 100

# you can loop through all values in a tuple using for loop

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# you can assign new values to a tuple and redefine the entire thing

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)


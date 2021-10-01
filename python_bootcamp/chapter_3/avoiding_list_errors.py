#index errors are a common problem in python scripts

motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles[3])

#index errors mean python can't find the element you requested in the list
# whenever you want to access the last item in a list, use index -1
# index -1 will only ever return an error for an empty list

print(motorcyles[-1])


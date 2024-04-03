# Sets - Exercise

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {"John", "Michael", "Terry", "Eric", "Graham"}
my_friends = {"Reg", "Loretta", "Colin", "John", "Graham"}
cars = ["900", "420", "V70", "911", "996", "V90", "911", "911", "S", "328", "900"]


# 1 
print('Eric' in friends and 'John' in friends)


# 2 
print(friends.union(my_friends))
print(friends | my_friends)

# 3 Intersection
print(friends & my_friends)


# use difference 
print(friends - my_friends)
print(my_friends - friends)


# semetric difference
print(my_friends ^ friends)

# conevert cars list to set 
cars_no_dupl = set(cars)
print(cars_no_dupl)


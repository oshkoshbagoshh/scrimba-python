# comprehension lists


numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)

# second way
new_list = [num*num for num in numbers]
print(new_list)

# print even numbers
# give me a list with num for each num in numbers if num is even 
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

# odd numbers
new_list1 = [num for num in numbers if num %2 != 0]
print(new_list1)

# using a filter
new_list2 = filter(lambda num: num % 2 == 0,numbers)
print(new_list2) # filter returns an object, so need to turn into list
print(list(new_list2))


# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)

# second way

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)
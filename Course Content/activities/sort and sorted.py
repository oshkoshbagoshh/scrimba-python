# Sort() and Sorted()
my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog': 2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'


# lists 
print(my_list, 'original')
print(my_list.sort())
print(my_list,'new', "sorted list")
my_list1 = sorted(my_list)
print(reversed(my_list)) # reversed object so need to turn into list
print(list(reversed(my_list)), 'reversed list')
print(my_list[::-1], 'second way of reversing a list')
# print(my_list1)

# tuples 
print(my_tuple, 'original tuple')
print(sorted(my_tuple), 'sorted tuple')
print(my_tuple, 'new tuple')


# string
print(my_string,'original string')
print(sorted(my_string), 'sorted string')
print(my_string,'new string')

# dictionary
print(my_dict,'original dictionary')
print(sorted(my_dict), 'sorted dictionary')
print(sorted(my_dict.items()), 'sorted by items')
print(sorted(my_dict.values()), 'sorted by values')
print(sorted(my_dict.values(), reverse=True), 'sorted by values reversed')
print(my_dict,'new dictionary')


# using keys to sort
my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list))
print(sorted(my_list, key= abs)) # sorted by key 
print(sorted(my_llist)) # list within a list
print(sorted(my_llist, key= lambda item: item[2])) # sorting with lambda function



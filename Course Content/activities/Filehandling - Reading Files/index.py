# reading files 

my_file = open('greeting.txt', 'r') # read mode, write mode, append mode 
print(my_file.read())
print(my_file.read(10)) # first 10 characters
print(my_file.readline()) # line by line 
print(my_file.readline()) # line by line 


# line by line 
line_by_line = my_file.readline()
line_by_line1 = my_file.read().splitlines()
print('readlines: ', line_by_line)
print('splitlines: ', line_by_line1)

# always close the file 
my_file.close()


# context manager
with open('friends.csv','r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')


# loop through lines 
with open('movies.txt','r') as f:
    # for line in f 
    for line in f:
        print(line)
        
        
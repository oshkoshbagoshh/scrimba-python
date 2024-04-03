# demoing the split and join functions
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

print(list(msg)) # breaks it up by turning it into a list
print(msg.split()) # created a list of each word
print(msg.split(' ')) # can split by what you want to split by 

print(csv.split(','))

print('-'.join(friends_list))
print(''.join(friends_list))


print(''.join(msg.split()))
print(msg.replace("  ", "'"))




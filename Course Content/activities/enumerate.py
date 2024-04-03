print('python101 - enumerate\n')

friends = ['Brian','Judith','Reg','Loretta','Colin']

print(friends)
print("\n")

i = 51
# for friend in friends:
#     print(i,friend)
#     i = i+ 1
    
for num, friend in enumerate(friends, 51):
    print(num, friend)
    
print(type(enumerate(friends)))
print(list(enumerate(friends)))

for num, letter in enumerate('python', start=5):
    print(num, letter)
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
# friends.sort()
friends.sort(reverse=True)
print(friends)
friends.reverse() 
print(friends)
print(min(cars))
print(max(cars))
print(sum(cars))
print(min(friends))
print(max(friends))

friends.append('Mike williams')
friends.insert(1, 'Bill')
friends[2]='TerryG'
extended_list = friends.extend(str(cars))

new_friends = list(friends)
friends.remove('Terry')
friends.pop(-1)
friends.clear()
# del friends[2]




print(friends)
print(new_friends)
print(extended_list)




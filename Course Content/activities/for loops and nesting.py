for letter in 'Norwegian blue':
    print(letter)
    
    
print("For Loop done!")


for furgle in range(8):
    print(furgle)
    
for furgle in range(1-8, 2):
    print(furgle)
    

friends = ['Ross', 'Rachel', 'Monica', 'Chandler', 'Joey']
for index in range(len(friends)):
    print(friends[index])

    

for friend in friends:
    if friend == 'Chandler':
        print(f"found {friend}")
        
        continue 
    

        
# nested for loops
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")

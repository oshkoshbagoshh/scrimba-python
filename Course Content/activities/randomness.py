# randomness
import random
import string

print("**randomness**")


print(random.randint(1,10))


for i in range(5):
    print(random.random()*6)

# using uniform
for i in range(6):
    print(random.uniform(1,6))

# dice roller
for i in range(6):
    print(random.randint(1,6))
        
for i in range(5):
    print(random.randrange(1,100,2))
    
    
# using choice to randomly select item in a list
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

print(random.choice(friends_list))

# use sample to avoid duplicates
print(random.sample(friends_list,5))

# shuffle
random.shuffle(friends_list)
print(friends_list)


# generate a user name
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'


letters_and_numbers = string.ascii_lowercase + string.ascii_uppercase + digits

print(letters_and_numbers)


# generate random words
word = ''
for i in range (7):
    word += random.choice(string.ascii_letters)

print(word)

# using sample to prevent dupes
word1 = ''.join(random.sample(letters_and_numbers,7))
print(word1)

word = random.choices(letters_and_numbers, k=7)   
print(word)
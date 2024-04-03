# dictionaries
# used for key value pairs

movie = {
    'title': "Life of Brian",
    'year': 1979,
    'cast': ['John','Michael','George','Terry']
}


print("{Dictonaries}")
print(movie)
print(movie['title'])
print(movie.get('budget', 'not found')) # get method to return a value and what you want to return
movie['title'] = 'The Holy Grail'
movie['budget'] = 250000
print(movie.get('title'))
print(movie.get('budget'))
print(type(movie))
print(movie)
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
print(movie)
# deletin entries
del movie['year']
movie['year'] = '1980'
# pop command (this removes it but lets us save in a variable)
year = movie.pop('year')
print(year)
movie['year'] = 1999

# get length 
print(len(movie))
print(movie.keys())
print(movie.values())

# looping through a dictinary 

for key, value in movie.items():
    print(key)
    
# iterating through dictionaries
for key, value in movie.items():
    print(f"{key}: {value}")

print("\n\n")

# ==================
# Dictionaries 2 
# ===============
python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# membership test (case censitive)
print('arthur' in holy_grail)
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here!')


# concatenating dictionaries
people = {}
people1 = {}
people2 = {}

# method 1 - update 
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)

print(people)

# method 2 - comprehension
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(people1)

# method 3 - unpacking 
people2 = {**python,**holy_grail, **life_of_brian}

print(people2)

# sortin 
print(sorted(people)) # only get the keys
# in order to get everything, need to print items
print(sorted(people.items()))
print(sorted(people2.items()))
print(sorted(people2.items()))

# find sum of all of the values 
print('The sum of the ages: ', sum(people.values()))
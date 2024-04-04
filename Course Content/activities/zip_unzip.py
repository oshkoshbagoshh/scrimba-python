# zip and unzip 

print("**zip and unzip**")
print("----------")
# ----------------


# nums = [1,2,3,4] 
nums = '1234'
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
# nam = 'jack'
combo = list(zip(nums, letters, names))
combo_dict = dict(zip(nums,letters))
print(combo)
print(combo_dict)

# unzip to take part
num,let,nam = zip(*combo)
print(num, let, nam)


# dictionarites
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys, values)
en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)

en,sv = list(en_sv_dict.keys(), list(en_sv_dict.values()))
print(en,sv)
en1, sv1 = zip(*en_sv_dict.items())
print(en1, sv1)




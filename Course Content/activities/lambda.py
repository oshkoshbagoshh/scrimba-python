# lambda functions
print("**Lambda functions part 1 **")


# original way
def square(x):
    return x*x

print(square(5))

# lambda way
square = lambda x: x*x
print(square(3))


name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
print(name_and_alias1('stew','stewkan45'))


# using lambda to sort 
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

# normal sort order
monty_python.sort(key = lambda name:name.split(" ")[1])
print(monty_python)

# reversed sort order
monty_python.sort(key = lambda name:name.split(" ")[-1])
print(monty_python)




# part 2 
# def func(n):
    # return lambda a: a*n
# a*2    
# print(type(func(3)))

# consulting fees

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walkin_cost(2))
print(premium_cost(2))
print(price_calc(1,25)(2))

print((lambda a,b,c: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
print((lambda *args: sum(args))(2,3,4,50))
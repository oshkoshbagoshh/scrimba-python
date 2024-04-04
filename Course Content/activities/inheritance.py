# class inheritance
print("**Class Inheritance**")

print("-------------------")

# ---------------------------------


class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")

# create Doctor class that inherits from Person Class
class Doctor(Person):
    # pass # have this by default if they inhereit everythin from Parent Class and nothin more
    def heal(self):
        print("Heals 10 health points")


# second class
class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Move 6 spaces")

# multiple inheritance
class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisible")
    
    def heal(self):
        print("Heals 15 points")

character1 = Person()
character1.move()
character1.rest()
character2 = Doctor()
character2.heal()
character2.move()
character3 = Fighter()
character3.fight()
character4 = Wizard()
character4.cast_spell()
character4.heal()
character4.move()




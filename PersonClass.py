# This is a part of a fictitious family sorting process
# Here, only one instance of a last name can exist
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def getFName(self):
        return self.firstName
    
    def getLName(self):
        return self.lastName
        
    # Objects are considered equal if they have the same last name
    # They are in the same equivalence class/ coset depending on how you look at it
    def __eq__(self, other):
        return self.getLName() == other.getLName()
        
Henry = Person("Henry", "Jones")

June = Person("June", "Jones")

print("Hi, my name is " + Henry.getFName() + " " +  Henry.getLName())

print("Hi, my name is " + June.getFName() + " " +  June.getLName())

print(Henry == June)




        
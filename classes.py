class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    
    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getAge(self):
        return self.age

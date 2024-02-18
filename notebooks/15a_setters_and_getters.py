class Person:
    def __init__(self, age):
        self.age = age
    
    @property
    def age(self):
        print("Getting the age...")
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            print("We cannot have negative ages")
        else:
            print("Setting the age...")
            self._age = age
    
    def category(self):
        if self.age < 13:
            return "Kid"
        elif self.age >= 13 and self.age < 18:
            return "Teen"
        elif self.age >= 18 and self.age < 65:
            return "Adult"
        else:
            return "Elderly"
        
person_1 = Person(25)
person_2 = Person(1)
person_3 = Person(-1)
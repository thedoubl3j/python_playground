# Go through and label all if the following classes/objects with a has-a or is-a relation ship.

#Animal is-a object.
class Animal(object):
    pass

#Dog is a animal
class Dog(Animal):

    def __init__(self, name):
        #dog has a name
        self.name = name

# Cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        #cat has a name
        self.name = name

# Person is a object (similar to Animal)
class Person(object):

    def __init__(self, name):
        # person has a name
        self.name = name
        # person has a per of some kind
        self.pet = None

# Employee is a person (instance of person)
class Employee(Person):

    def __init__(self, name , salary):
        #
        super(Employee, self).__init__(name)
        #Employee has a salary
        self.salary = salary

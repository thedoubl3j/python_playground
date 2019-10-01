class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    # everytime you instantiate an object from this class, this is run. often a good place to set variables.
    # because they can be used throughout the class from there. 
    def __init__(self, age=10):
        self.age = age

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

class Kid(Child):
    def month(self):
        return self.age


dad = Parent()
son = Child()
daughter = Kid()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
print(son.age)
print(daughter.month())
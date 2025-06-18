''' This code demonstrates hierarchical inheritance in Python,
where multiple child classes inherit from a single parent class.
Each child class can override methods from the parent class.'''
class Animal:
    def sound(self):
        print("Animal makes a sound")

#child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

#child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

#child class 3
class Cow(Animal):
    def sound(self):
        print("Cow moos")

def main():
    # Creating instances of each child class
    d1 = Dog()
    c1 = Cat()
    c2 = Cow()

    # Calling the sound method for each instance
    d1.sound()  # Output: Dog barks
    c1.sound()  # Output: Cat meows
    c2.sound()  # Output: Cow moos
"""This code demonstrates multiple inheritance in Python using a base class and a derived class that inherits from two base classes.
The derived class overrides methods from the base classes to provide specific functionality."""
#Base class 1
class Animal:
    def sound(self):
        print("Animal makes a sound")

#Base class 2
class Bird:
    def fly(self):
        print("Bird flies")

#Derived class inheriting from (multilevel and multiple inheritance)
class Parrot(Animal, Bird):
    def sound(self):
        print("Parrot squawks")
    
    def fly(self):
        print("Parrot flies high")
class Sparrow(Animal, Bird):
    def sound(self):
        print("Sparrow chirps")
    
    def fly(self):
        print("Sparrow flies swiftly")

def main():
    # Creating instances of each derived class
    parrot = Parrot()
    sparrow = Sparrow()

    # Calling the sound and fly methods for each instance
    parrot.sound()  # Output: Parrot squawks
    parrot.fly()    # Output: Parrot flies high

    sparrow.sound()  # Output: Sparrow chirps
    sparrow.fly()    # Output: Sparrow flies swiftly
    
if __name__ == "__main__":
        main()
# This code demonstrates inheritance in Python with a parent class and two child classes.
# A constructor is defined in each class, and the child classes override a method from the parent class.
class parent:
    #constructor
    def __init__(self):
        self.name = "Parent Class"
    def display(self):
        print("This is the parent class method.")
class child1(parent):
    #constructor
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.name = "Child Class 1"
    def display(self):
        print("This is the child class 1 method.")
class child2(parent):
    #constructor
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.name = "Child Class 2"
    def display(self):
        print("This is the child class 2 method.")
def main():
    # Creating instances of each child class
    c1 = child1()
    c2 = child2()

    # Calling the display method for each instance
    c1.display()  # Output: This is the child class 1 method.
    c2.display()  # Output: This is the child class 2 method.

main()

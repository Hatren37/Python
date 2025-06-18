#This program demonstrates the use of single level inheritance in Python.
class A:
    def m1(self):
        print("Method m1 from class A")
    def m2(self):
        print("Method m2 from class A")

class B(A):
    def m3(self):
        print("Method m3 from class B")

def main():
    peter = A()  # Creating an instance of class A
    peter.m1()  # Calling method m1 from class A
    peter.m2()  # Calling method m2 from class A
    #peter.m3()  # This will raise an AttributeError since m3 is not defined in class A
    john = B()  # Creating an instance of class B which is a child class of A
    john.m3()  # Calling any method from a child class is possible because it inherits from class A

main()
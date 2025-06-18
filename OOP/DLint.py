#This program demonstrates the use of multiple level inheritance in Python.
class A:
    def m1(self):
        print("Method m1 from class A")
    def m2(self):
        print("Method m2 from class A")

class B(A):
    def m3(self):
        print("Method m3 from class B")
class C(B):
    def m4(self):
        print("Method m4 from class C")

def main():
    peter = C()  # Creating an instance/object of class C because it will inherit from class B and A
    peter.m1()  # Calling method m1 from class A
    peter.m2()  # Calling method m2 from class A
    peter.m3()  # Calling method m3 from class B
    peter.m4()  # Calling method m4 from class C
main()
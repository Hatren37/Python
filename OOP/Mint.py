#This program demonstrates the use of multiple inheritance in Python.
class A:
    def m1(self):
        print("Method m1 from class A")

class B:
    def m2(self):
        print("Method m2 from class B")

class C(A, B):  # Class C inherits from both A and B
    def m3(self):
        print("Method m3 from class C")

def main():
   petra = C()  # Creating an instance of class C
   petra.m1()  # Calling method m1 from class A
   petra.m2()  # Calling method m2 from class B
   petra.m3()  # Calling method m3 from class C
   

main()
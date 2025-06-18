class A:
    x = 100 #class level variable
    def __init__(self):
        self.y = 200 #object level variable
def main():
    print(A.x)  # Accessing class level variable

    a1 = A()  # Creating an instance of class A
    print(a1.y)  # Accessing object level variable

    a1.y = 300  # Modifying object level variable
    print(a1.y)  # Output: 300

    print(a1.x)  # Accessing class level variable through instance
    
    A.x = 400  # Modifying class level variable
    print(a1.x)  # Output: 400

main()
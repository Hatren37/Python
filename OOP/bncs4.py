class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    #Taking input from the user
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    p1 = person(name, age)  # Creating an instance of the person class
    p1.display()  # Displaying the person's details

main()
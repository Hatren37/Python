#function with arguments and without return value
def add_numbers(a, b):
    print("The sum is:", a + b)

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    add_numbers(num1, num2)
main()
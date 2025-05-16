#function with arguments with return value
def add_numbers(a, b):
    return a + b
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print("The sum is:", result)
main()

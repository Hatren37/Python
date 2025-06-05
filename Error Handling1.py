#raise errorname()
def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        raise ValueError()
    else:
        return num1 * num2
    
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = multiply(num1, num2)
        print(f"The result of multiplying {num1} by {num2} is: {result}")
    except ValueError:
        print("Multiplication by zero is not allowed.")

main()
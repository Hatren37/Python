#Program to demonstrate error handling in Python by dividing two numbers
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is: {result:.2f}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid integers.")

finally:
    print("Execution completed. Thank you for using the program.")
    
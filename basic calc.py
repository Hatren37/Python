print("*************Calculator*************")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
opt=int(input("Enter your option: "))
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
match(opt):
    case 1:
        print("Sum of ",num1," and ",num2," is ",num1+num2)
    case 2:
        print("Diff of ",num1," and ",num2," is ",num1-num2)
    case 3:
        print("Product of ",num1," and ",num2," is ",num1*num2)
    case 4:
        if num2==0:
            print("Division by zero is not allowed")
        else:
            print("Division of ",num1," and ",num2," is ",num1/num2)
    case _:
        print("Invalid option")
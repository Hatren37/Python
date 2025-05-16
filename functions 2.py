# function without arguments but with a return value
def addn():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b

def main():
    result = addn()
    print("The sum is:", result)

main()
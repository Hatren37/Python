#print("**********Login**********")
"""user=input("Username: ")
password=input("Password: ")
if user=="nit":
    if password=="nit123":
        print("Welcome")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")"""
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b:
    if a>c:
        print("Largest number is ",a)
    else:
        print("Largest number is ",c)
elif b>c:
    if b>a:
        print("Largest number is ",b)
    else:
        print("Largest number is ",a)
elif c>a:
    if c>b:
        print("\nLargest number is ",c)
    else:
        print("\nLargest number is ",b)
else:
    print("\nAll numbers are equal")
# This code takes a number as input and prints its multiplication table using a while loop.
"""num=int(input("Enter a number: "))
i=1
while i<=num:
    p=num*i
    print(num,"*",i,"=",p)
    i+=1"""

#a program to calculate the factorial of a number using a while loop
num=int(input("Enter a number: "))
fact=1
while num>0:
    fact*=num
    num-=1
    print("Factorial is:",fact)
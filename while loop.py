"""i=1
while i<=5:
    print("ISBAT")
    i+=1
"""
num=int(input("Enter a number: "))
s=0
while num!=0:
    r=num%10
    s+=r
    num=num//10
    # r=num%10 gives the last digit of the number
    print("Sum of digits is:",s)
# The above code takes a number as input and calculates the sum of its digits using a while loop.

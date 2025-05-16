choice= "yes"
while choice!= "no":
    num=int(input("Enter a number: "))
    i=1
    while i<=num:
        p=num*i
        print(num,"*",i,"=",p)
        i+=1
    choice=input("Enter your choice(yes/no): ")
# This code takes a number as input and prints its multiplication table using a while loop.
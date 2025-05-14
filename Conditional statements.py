p=float(input("Enter marks: "))
if p>=90 and p<=100:
    if p==100 and p>=95:
        print("Grade A+")
    else:
        print("Grade A")
elif p>=80 and p<90:
    print("Grade B")    
elif p>=60 and p<80:
    print("Grade C")
else:
    print("Grade D")
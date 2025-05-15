#a program to count number of vowels in a string using a while loop
str1=input("Enter a string: ")
vowels=0
for ch in str1:
    if ch in 'aeiouAEIOU':
        vowels+=1
print("Number of vowels in the string is:",vowels)

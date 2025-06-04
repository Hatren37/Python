#program to check if a string is a palindrome or not
str1=input("Enter a string: ")
str2=str1[::-1] 
str3=str1.lower()  # Convert to lowercase for case-insensitive comparison
print(str3)
print(str3.capitalize())
print(str3.index)
print(str3.upper())
print(str3.isalnum())
print(str3.isalpha())
print(str3.isdigit())
#print(str3.decimal())
if str1==str2:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
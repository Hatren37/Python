from m1 import iseven
def main():
    num = int(input("Enter a number: "))
    if iseven(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
main()
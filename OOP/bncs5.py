# This code demonstrates the use of default arguments in a function.
def product(a, b, c=None):
    if c is None:
        print(a * b)
    else:
        print(a * b * c)

def main():
    product(2, 3)      # Output: 6
    product(2, 3, 4)   # Output: 24

main()

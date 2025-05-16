def simple_interest(amount, rate, time):
    """
    Calculate simple interest.

    Parameters:
    amount (float): The principal amount.
    rate (float): The rate of interest per year.
    time (float): The time in years.

    Returns:
    float: The simple interest calculated.
    """
    s=(amount * rate * time) / 100
    return s
def main():
    si1=simple_interest(9000,12,2.0)
    si2=simple_interest(9000,14,2)
    print(f"simple_interest is {si1}")
    print("The simple interest-2 is", si2)
main()
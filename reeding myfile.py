import csv
def main():
    f = open("contacts.csv", "r")  # Open the file in read mode
    try:
        cr = csv.reader(f)  # Create a CSV reader object
        for row in cr:  # Iterate through each row in the CSV file
            print(row)  # Print the row to the console
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    finally:
        f.close()  # Close the file
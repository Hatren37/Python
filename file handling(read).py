def main():
    f = "D:/Python Assignments/Python/Announcement.txt" # Initialize f to the file path
    try:
        with open("Announcement.txt", "r") as f:
            s = f.read()  # Read the content of the file
            print(s)  # Print the content to the console
    except OSError:
        print("The file does not exist.")
    finally:
        if f:  # Check if f is not None
            f.close()  # Close the file if it was opened
            
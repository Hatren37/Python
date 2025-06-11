#file creation 
def main():
    try:
        file = open("Announcement.txt", "w")
        # Alternatively 
        # with open("example.txt", "w") as file:
        file.write("Hello, World!"
        "Tommorrow is a public holiday.")
    except OSError:
        print("Unable to create or write to the file.")
    finally:
        file.close()
        print("File created and written successfully.")

main()
# This code creates a file named "Announcement.txt" and writes a message into it.
        
#program to store student details in a file
def main():
    try:
        f = open("Exam.txt", "w") # Open the file in write mode
        f.write("Roll No.\tName\tCourse\n")  # Write the header row
        while True:
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            print(f"{roll_no}\t{name}\t{course}", file=f)  # Write the student details
            ch = input("Do you want to add another student? (y/n): ")
            if ch.lower() != 'y':
                break
    except OSError:
        print("An error occurred while creating the file.")
    finally:
        f.close()

main()
# program to read student details from a file

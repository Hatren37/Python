#program to append contents of Exam.txt file
def append_exam_file():
    try:
        f = open("Exam.txt", "a")  # Open the file in append mode
        while True:
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            print(f"{roll_no}\t{name}\t{course}", file=f)  # Append the student details
            ch = input("Do you want to add another student? (y/n): ")
            if ch.lower() != 'y':
                break
    except OSError:
        print("An error occurred while appending to the file.")
    finally:
        f.close()

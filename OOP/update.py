import mysql.connector  # Importing the MySQL connector library

def main():
    cn = mysql.connector.connect(database='Student_records', user="root", password='***************')  # Password hidden for security reasons
    c = cn.cursor()
    
    while True:
        roll_no = input("Enter the roll number of the student to update (or 'exit' to quit): ")
        if roll_no.lower() == 'exit':
            break
        
        name = input("Enter the name of the student: ")
        sub1 = input("Enter the subject 1 marks: ")
        sub2 = input("Enter the subject 2 marks: ")
        sub3 = input("Enter the subject 3 marks: ")
        sub4 = input("Enter the subject 4 marks: ")
        
        # Update the student's marks in the database
        c.execute("UPDATE stud_marks SET name = %s, sub1 = %s, sub2 = %s, sub3 = %s, sub4 = %s WHERE roll_no = %s", 
                  (name, sub1, sub2, sub3, sub4, roll_no))
        
        if c.rowcount > 0:
            print(f"Student with roll number {roll_no} has been updated successfully.")
            # Commit the changes to the database
            cn.commit()
        else:
            print(f"No student found with roll number {roll_no}. \nPlease check the roll number and try again.")

        if input("Do you want to update another student? (yes/no): ").lower() != 'yes':
            break
    # Close the cursor and connection
    c.close()
    cn.close()

main()
        

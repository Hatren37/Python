# This program connects to a MySQL database and deletes records based on user input.
import mysql.connector  # Importing the MySQL connector library
def main():
        # Establish connection to the MySQL database
        cn = mysql.connector.connect(database='Student_records', user="root", password='************')  # Password hidden for security reasons
        c = cn.cursor()
        while True:
                roll_no = int(input("Enter roll number to delete: "))  # Prompt user for roll number to delete
                # Execute the delete command
                c.execute("DELETE FROM stud_marks WHERE roll_no = %s", (roll_no,))

                if c.rowcount > 0:
                        print(f"Record with roll number {roll_no} deleted successfully.")
                        cn.commit()  # Commit the changes to the database
                else:
                        print(f"No record found with roll number {roll_no}.")

                ans = input("Do you want to delete another record? (yes/no): ")
                if ans.lower() != 'yes':
                        break

main()

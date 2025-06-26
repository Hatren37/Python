# This code enables a user to edit records in a MySQL database using dynamic SQL queries.
import mysql.connector  # Importing the MySQL connector library
def main():
    try:
        # Establish connection to the MySQL database
        cn = mysql.connector.connect(database='Student_records', user="root", password='************')  # Password hidden for security reasons
        c = cn.cursor()
    
        while True:
            # Prompt user for input
            roll_no = int(input("Enter roll number: "))
            name = input("Enter name: ")
            sub1 = int(input("Enter marks for subject 1: "))
            sub2 = int(input("Enter marks for subject 2: "))
            sub3 = int(input("Enter marks for subject 3: "))
            sub4 = int(input("Enter marks for subject 4: "))
            Id = roll_no

            cmd = "INSERT INTO stud_marks VALUES (%s, %s, %s, %s, %s, %s)"
            c.execute(cmd,params= (roll_no, name, sub1, sub2, sub3, sub4))
            k = c.rowcount
            if k == 1:
                print("Record inserted successfully.")
                cn.commit()  # Commit the changes to the database
            ans = input("Do you want to insert another record? (yes/no): ")
            if ans.lower() != 'yes':
                break

    except ValueError as ve:
        print(f"\nValue Error: {ve}. Please enter valid data.")

    except mysql.connector.Error as err:
        print(f"\nMySQL Error: {err}. Please check your database connection and query.")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}. Please try again.")

    finally:
        if cn:
            cn.close()
            print("\nConnection closed.")
main()
#This program connects and inserts records into a MySQL database.
import mysql.connector # Importing the MySQL connector library
def main():
    try:
        #est coonnection to the MySQL database
        cn = mysql.connector.connect(database='Student_records', user="root", password='***********') # Password hidden for security reasons
        c = cn.cursor()
        # Insert records into the database
        c.execute("insert into stud_marks VALUES (6, 'glamour', 100, 99, 100, 98), (7, 'sky', 88, 89, 90, 85), (8, 'lawrence', 78, 79, 80, 75)")
        cn.commit()  # Commit the changes to the database
        print("Record inserted successfully.")

    except:
        print("Failed to connect to the database.")
    finally:
        if cn:
            cn.close()
            print("Connection closed.")

main()

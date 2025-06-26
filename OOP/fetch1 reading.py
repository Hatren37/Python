# A python script to fetch the first reading from a database
import mysql.connector  # Importing the MySQL connector library
def main():
    cn = mysql.connector.connect(database='Student_records', user="root", password='Justlogin/37')  # Password hidden for security reasons
    c = cn.cursor()
    c.execute("SELECT * FROM stud_marks")  # Execute a SQL query to select all records from the 'stud_marks' table

    ''' stud1 = c.fetchone()  # Fetch the first record from the database
    print(stud1)  # Print the fetched record

    a= c.fetchmany(4)  # Fetch a selected number of records from the database
    print(a)  # Print the fetched records'''
    b = c.fetchall()  # Fetch all records from the database
    print(b)  # Print all fetched records

main()
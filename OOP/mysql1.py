#
import mysql.connector
def main():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(database='student_records',user="root",password='********') #Password hidden for security reasons
        print("Connected to the database successfully.")
        # Print the connection details
        print(f"User: {conn.user}")
        print(f"Host: {conn.server_host}")
        print(f"Port: {conn.server_port}")
        # Print the database name
        print(f"Database: {conn.database}")
        

    except:
        print("Failed to connect to the database.")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

main()


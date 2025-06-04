#Email book Application
email_set = set()  # Initialize an empty set to store email addresses
while True: # Start an infinite loop to keep the application running
    print("******** Email Book Application********")
    print("1. Add Email")
    print("2. Search Email")
    print("3. Delete Email")
    print("4. Display All Emails")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        email = input("Enter email address to add: ")
        if email in email_set:
            print("Email already exists.")
        else:
            #We can also use .update() method to add multiple emails at once but it requires an iterable
            #like a list or another set, and it will not raise an error if the email already exists
            email_set.add(email)
            print("Email added successfully.")
    elif choice == 2:
        email = input("Enter email address to search: ")
        if email in email_set:
            print(f"Email {email} found.")
        else:
            print("Email not found.")
    elif choice == 3:
        email = input("Enter email address to delete: ")
        if email in email_set:
            #we can also use remove() method to delete an email but it raises an error if the email is not found
            email_set.discard(email)
            print(f"Email ID {email} deleted successfully.")
        else:
            print("Email not found.")
    elif choice == 4:
        if email_set:
            print("All Emails:")
            for email in email_set:
                print(email)
        else:
            print("No emails found.")
    elif choice == 5:
        print("Exiting the Email Book Application.")
        break
    else:
        print("Invalid choice. Please try again.")
# End of the Email Book Application
# Note: This code uses a set to store email addresses, ensuring that each email is unique.
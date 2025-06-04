stack=[]
while True:
    print("**** Stack Operations ***")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            element = input("Enter the element to push: ")
            stack.append(element)
            print(f"{element} pushed onto stack.")
        case 2:
            if stack:
                popped_element = stack.pop()
                print(f"{popped_element} popped from stack.")
            else:
                print("Stack is empty. Cannot pop.")
        case 3:
            if stack:
                print("Current stack:", stack)
            else:
                print("Stack is empty.")
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
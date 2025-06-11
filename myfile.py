import csv
def main():
    try:
        f = open("contacts.csv","w",newline='')                    # Open the file in write mode
        cw = csv.writer(f)                                          # Create a CSV writer object
        cw.writerow(["Emp No.", "Name", "Salary"])                  # Write the header row
        cw.writerow([101, "John Doe", 50000])  
        cw.writerow([102, "Jane Smith", 60000])     
        cw.writerow([103, "Alice Johnson", 55000])  
        cw.writerow([104, "Bob Brown", 70000]) 
    except OSError as e:
        print(f"An error ocuurred while creating the csv file")
    finally:
            f.close()
main()

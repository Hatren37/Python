import json

tracy = {
    "name": "Namukwaya Tracy",
    "age": 30,
    "city": "kampala",
}

file_path = "Tr.json"
with open(file_path, "w") as file:
    json.dump(tracy, file) # Writing the dictionary to a JSON file
    
with open(file_path, "r") as file:
    data = json.load(file)  # Reading the JSON file back into a dictionary
    print(data)  # Output: {'name': 'Namukwaya Tracy', 'age': 30, 'city': 'kampala'}
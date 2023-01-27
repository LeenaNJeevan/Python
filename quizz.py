import json

# Open the json file
with open('file1.json', 'r') as f:
    content = json.load(f)

# Now you can access the data in the file as a Python object
print(content)

# print specific key value form the file
print("Printing name from the file1", content["name"])

# modify the key city
content['age'] = "100"
print("Modified age", content["age"])

# Write the data to a new file
with open('file2.json', 'w') as f:
    json.dump(content, f)

print("Contents of file2", content)
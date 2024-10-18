# Define the file name
file_name = "example.txt"

# Write to the file
with open(file_name, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")

# Read from the file
with open(file_name, 'r') as file:
    content = file.read()

# Print the content read from the file
print("Content of the file:")
print(content)
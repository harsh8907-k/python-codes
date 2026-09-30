import os

# Specify the directory
path = "."

# Get the contents of the directory
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")

for item in contents:
    print(item)
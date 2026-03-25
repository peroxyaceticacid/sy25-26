file_name = input("Enter the file name: ")
pattern = input("Enter the pattern: ")

with open(file_name, 'r') as file:
    for line in file: 
        if pattern in line: print(line.strip())
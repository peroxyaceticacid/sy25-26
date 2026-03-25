count = 0
files = [
    "bee movie.txt",
    "gettysburg address.txt"
    ]

print(*(f'[{i}] {n}' for i, n in enumerate(files)), sep='\n')
file_name = files[int(input('Choose file by number: '))]
word = input('Enter word to search: ')

with open(file_name, 'r') as f:
    while True:
        line = f.readline().lower()
        if not line:
            break
        count += line.count(word.lower())

print(f'{word} appears {count} times in "{file_name}".')
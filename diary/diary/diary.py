import datetime

file = "diary.txt"
running = True

#// functions

def write():
    with open(file, 'a') as f:
        entry = input("\nWrite your diary entry:\n")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {entry}\n")

def read():
    with open(file, 'r') as f:
        entries = f.readlines()
        for entry in entries:
            print(f'{entry.strip()}\n')

def clear():
    with open(file, 'w') as f:
        f.write("")

def exit_program():
    global running
    running = False
    print("Exiting")

#// menu setup

menu_options = {
    1: lambda: write(),
    2: lambda: read(),
    3: lambda: clear(),
    4: lambda: exit_program()
    }

#// main loop

while running:
    print('1. Write, 2. Read, 3. Clear, 4. Exit')
    choice = input("Choose an option (1-4): ")

    if not (1 <= int(choice) <= 4): print("Invalid\n"); continue

    menu_option = menu_options.get(int(choice))
    if menu_option: menu_option(); continue
    
    print("Not an option. Try again")

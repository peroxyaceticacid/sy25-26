# WRITTEN BY AIDEN JONES

#// variables

lineup = [] # list of tuples
running = True

#// functions

def view_lineup():
    print("\nCurrent Lineup:")
    for n, g, t in lineup:
        print(f"Band: {n} ({g}) - {t}m")

    print(f"Total Duration: {sum(t for _, _, t in lineup)}m\n")

def add_band(name, genre, duration):
    new_band = (name, genre, duration)
    lineup.append(new_band)
    print(f"Added band: {name}\n")

def remove_band(name):
    try:
        name = int(name)
        name -= 1  # adjust because user counts from 1
        if 0 <= name < len(lineup):
            removed_band = lineup.pop(name)
            print(f"Removed band: {removed_band[0]}\n")
    except ValueError:
        for band in lineup:
            if band[0] == name: lineup.remove(band); print(f"Removed band: {name}\n"); return

        print(f"Invalid band.\n")

def move_band(name, pos):
    pos = int(pos)
    pos -= 1 # adjust because user counts from 1.. again

    try:
        name = int(name)
        name -= 1  # adjust because user counts from 1.. last time
        rb = lineup.pop(name)
        lineup.insert(pos, rb)
    except ValueError:
        for band in lineup:
            if band[0] != name: break
            
            rb = lineup.pop(lineup.index(band))
            lineup.insert(pos, rb)

def exit_program():
    global running
    running = False
    print("Exiting")

#// menu setup

menu_options = {
    1: view_lineup,
    2: lambda: add_band(
        input("Name: "),
        input("Genre: "),
        int(input("Duration: "))
    ),
    3: lambda: move_band(1, len(lineup)),
    4: lambda: remove_band(
        input("Name or position: ")
    ),
    5: lambda: move_band(
        input("Name or position: "),
        input("Position: ")
    ),
    6: exit_program,
    }

#// main loop

while running:
    print("""---Py-Fest Lineup Manager ---
    1. View lineup and total time
    2. Add a new band
    3. Move first band to end
    4. Remove band by name or position
    5. Move band to specific position
    6. Exit""")
    choice = input("Choose an option (1-6): ")

    if not (1 <= int(choice) <= 6): print("Invalid\n"); continue

    menu_option = menu_options.get(int(choice))
    if menu_option: menu_option(); continue
    
    print("Not an option. Try again")
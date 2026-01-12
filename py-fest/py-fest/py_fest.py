# WRITTEN BY AIDEN JONES

#// variables

lineup = [] # list of tuples
running = True

#// functions

def view_lineup():
    for n, g, t in lineup:
        print(f"Band: {n}, Genre: {g}, Duration: {t}m\n")

    print(f"Total Duration: {sum(t for _, _, t in lineup)}m")

def add_band(name, genre, duration):
    new_band = (name, genre, duration)
    lineup.append(new_band)
    print(f"Added band: {name}\n")

def remove_band(name):
    if name is str:
        for band in lineup:
            if band[0] == name:
                lineup.remove(band)
                print(f"Removed band: {name}\n")
                return
        print(f"Invalid band.\n")
    elif name is int:
        name -= 1  # adjust because user counts from 1
        if 0 <= name < len(lineup):
            removed_band = lineup.pop(name)
            print(f"Removed band: {removed_band[0]}\n")

def move_band(name, pos):
    pos -= 1 # adjust because user counts from 1.. again

    if name is str:
        for band in lineup:
            if band[0] == name:
                rb = lineup.pop(lineup.index(band))
                lineup.insert(pos, rb)
    elif name is int:
        name -= 1  # adjust because user counts from 1.. last time
        rb = lineup.pop(name)
        lineup.insert(pos, rb)

#// menu setup

menu_options = {
    1: view_lineup,
    2: lambda: add_band(
        input("Name: "),
        input("Genre: "),
        int(input("Duration: "))
    ),}

#// main loop

while running:
    print("""---Py-Fest Lineup Manager ---
    1. View lineup and total time
    2. Add a new band
    3. Move first band to end
    4. Remove band by name
    5. Move band to specific position
    6. Exit""")
    choice = int(input("Choose an option (1-6): "))

    if choice is not int or choice < 1 or choice > 6:
        print("Invalid\n")
        continue
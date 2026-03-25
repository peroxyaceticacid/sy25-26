# WRITTEN BY AIDEN JONES

#// variables

inventory = {}
running = True

#// functions

def view_inventory():
    print("\n--- Current Inventory ---")
    for n in inventory:
        print(f"- {n}: {inventory[n]}")
    print("-------------------------")

def add_item(name, am):
    if inventory.get(name.lower()) is None: inventory[name.lower()] = 0; print(f"Added {name} to inventory.")
    inventory[name.lower()] += am

    print(f"Updated {name} to {am}.\n")

def remove_item(name, am):
    if inventory.get(name.lower()) is None: print("Invalid item.\n"); return
    inventory[name.lower()] -= am
    if inventory[name.lower()] <= 0: del inventory[name.lower()]; print(f"Removed {name} from inventory.\n"); return
    
    print(f"Updated {name} to {am}.\n")

def exit_program():
    global running
    running = False
    print("Exiting")

#// menu setup

menu_options = {
    1: lambda: add_item(
        input("Name: "),
        int(input("Amount: "))
    ),
    2: lambda: remove_item(
        input("Name: "),
        int(input("Amount: "))
    ),
    3: view_inventory,
    4: exit_program,
    }

#// main loop

while running:
    print("Options: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Choose an option (1-4): ")

    if not (1 <= int(choice) <= 4): print("Invalid\n"); continue

    menu_option = menu_options.get(int(choice))
    if menu_option: menu_option(); continue
    
    print("Not an option. Try again")
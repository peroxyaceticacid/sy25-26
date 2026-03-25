F1 = ["F1", "VW Off-Road-Bug", 185, (104, 142), 6000, 9.0, 1880, 4]
A4 = ["A4", "Suzuki Ignis", 180, (153, 206), 7250, 8.0, 1597, 4]
D2 = ["D2", "Toyota Celica GT-Four", 245, (220, 299), 5600, 5.3, 1998, 4]
G3 = ["G3", "Mitsubishi Pajero", 185, (153, 208), 7000, 9.6, 3497, 6]
C3 = ["C3", "VW-Polo GTI", 185, (96, 103), 7600, 8.0, 1600, 4]
C1 = ["C1", "Subaru Impreza WRC", 220, (221, 300), 5500, 5.4, 1994, 4]
B3 = ["B3", "Toyota Corolla WRC", 210, (220, 299), 5700, 5.4, 1972, 4]
E2 = ["E2", "Ford Escort WRC", 220, (220, 299), 6250, 5.6, 1993, 4]
B1 = ["B1", "Seat Cordoba WRC", 230, (221, 300), 6000, 5.0, 1998, 4]
C2 = ["C2", "Opel Astra GSi", 235, (235, 320), 6200, 5.6, 2962, 6]

cars = [F1, A4, D2, G3, C3, C1, B3, E2, B1, C2]

def get_vehicle(data):
    ID, Name, Speed, O60, HP, CCs, RRM, Cylinders = map(str, data)

    rows = [
        f"{ID} | {Name}",
        f"{Speed} | {O60}",
        f"{HP} | {CCs}",
        f"{RRM} | {Cylinders}"
    ]

    width = max(len(row) for row in rows)
    border = "+" + "-" * (width + 2) + "+"

    print(border)
    for row in rows:
        print(f"| {row.ljust(width)} |")
    print(border)

i = 1
for car in cars:
    print(i, car[1])
    i += 1

while True:
    choice = int(input("\nSelect a vehicle by number: ")) - 1
    get_vehicle(cars[choice])

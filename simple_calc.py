def capacitor(c1, c2):  # capacitor in series calculations
    orientation = input("Type P for parallel or S for series: ")
    while orientation not in ("S", "P"):
        orientation = input("Type P for parallel or S for series: ")
    if orientation == "S":
        c12 = ((c1 ** -1) + (c2 ** -1)) ** -1
    else:
        c12 = c1 + c2

    print(f"Capacitance 1-2 = {c12} farads")


def resistor(r1, r2):  # resistor in parallel calculations
    orientation = input("Type P for parallel or S for series: ")
    while orientation not in ("S", "P"):
        orientation = input("Type P for parallel or S for series: ")
    if orientation == "P":
        r12 = ((r1 ** -1) + (r2 ** -1)) ** -1
    else:
        r12 = r1 + r2
    print(f"Resistance 1-2 = {r12} ohms")


while True:
    q_type = input("Type C for capacitor or R for resistor: ")
    if q_type == "C":
        capacitance1 = float(input("Capacitance 1 (farad): "))
        capacitance2 = float(input("Capacitance 2 (farad): "))
        capacitor(capacitance1, capacitance2)

    if q_type == "R":
        resistance1 = float(input("Resistance 1 (ohms): "))
        resistance2 = float(input("Resistance 2 (ohms): "))
        resistor(resistance1, resistance2)

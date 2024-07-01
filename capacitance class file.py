class Capacitance:
    def __init__(self, capacitance_1, capacitance_2, orientation):

        self.capacitance_1 = capacitance_1
        self.capacitance_2 = capacitance_2
        self.orientation = orientation

    def combine_capacitance(self):
        while True:
            if self.orientation == "p":  # if capacitors are in parallel
                capacitance = self.capacitance_1 + self.capacitance_2
                return capacitance

            elif self.orientation == "s":  # if capacitors are in series
                capacitance = (self.capacitance_1 ** -1 + self.capacitance_2 ** -1) ** -1
                return capacitance


num_cap = int(input("Number of capacitors: "))  # Number of capacitors

label_list = []  # list of labels for capacitors, voltages, & charges
prev = ""
for i in range(1, num_cap+1):
    next_num = prev + str(i)
    label_list.append(next_num)
    prev = next_num

current_capacitance = float(input("Enter capacitance1: "))
orientation_list = []
capacitance_list = [current_capacitance]

for i in range(1, num_cap):
    parallel_or_series = str(input("Capacitors in Series or Parallel (p/s):"))
    orientation_list.append(parallel_or_series)
    next_capacitance = float(input(f"Enter capacitance{i+1}: "))
    current_capacitor = Capacitance(current_capacitance, next_capacitance, parallel_or_series)
    current_capacitance = current_capacitor.combine_capacitance()
    capacitance_list.append(current_capacitance)

c_eq = current_capacitance
print(f"Total capacitance: {current_capacitance}")
voltage = float(input("Enter voltage: "))
total_charge = c_eq * voltage


if orientation_list[-1] == "s":
    print(f"Q eq = {total_charge:.2f}")
    print(f"Q {num_cap} = {total_charge:.2f}")
    print(f"Q {label_list[-2]} = {total_charge:.2f}")
else:
    ...

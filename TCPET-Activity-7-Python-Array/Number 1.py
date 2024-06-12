cutoff = 0
active = 0
breakdown = 0

voltage_values = []

for n in range(10):
    user_input = int(input("Enter a 10 voltage values simultaneously: "))
    voltage_values.append(user_input)

for i in range(10):
    if voltage_values[i] < 5:
        cutoff += 1
    elif voltage_values[i] > 5:
        breakdown += 1
    else:
        active += 1

print("\nRESULTS -----------------------------------------------------------------------------------------------------")
print(f"Active: {active}")
print(f"Cutoff: {cutoff}")
print(f"Breakdown: {breakdown}")

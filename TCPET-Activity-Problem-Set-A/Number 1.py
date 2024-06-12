
monthly_rate = float(input("Enter the monthly rate of the dormitory: "))

monthly_andrew = .40 * monthly_rate
monthly_andrei = .35 * monthly_rate
monthly_andres = .25 * monthly_rate

# Letter A - How much is the total monthly contribution of Andrew, Andrei and Andres
print(f"\nTotal monthly contribution of Andrew is {monthly_andrew}")
print(f"Total monthly contribution of Andrei is {monthly_andrei}")
print(f"Total monthly contribution of Andres is {monthly_andres}\n")

# Letter B - How much is the total rent in the dormitory for the whole school year,
# assuming it will last for 10 months
total_rent = monthly_rate * 10
print(f"The total rent in the dormitory for 10 months is {total_rent}\n")

# Letter C - How much will Andrew, Andrei and Andres prepare
# for the whole school year
total_andrew = monthly_andrew * 10
total_andrei = monthly_andrei * 10
total_andres = monthly_andres * 10

print(f"Andrew need to prepare {total_andrew} for the whole school year cost")
print(f"Andrei need to prepare {total_andrei} for the whole school year cost")
print(f"Andres need to prepare {total_andres} for the whole school year cost")
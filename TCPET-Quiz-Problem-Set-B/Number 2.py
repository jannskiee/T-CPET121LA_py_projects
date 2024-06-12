user_input = int(input("Multiplication Table, enter a number: "))

print("\nMultiplication Table of " + str(user_input))
for i in range(10):
    print(f"{user_input} x {i+1} = {user_input*(i+1)}")


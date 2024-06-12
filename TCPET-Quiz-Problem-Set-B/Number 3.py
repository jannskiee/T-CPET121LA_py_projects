for_user_input = int(input("For loop, enter a number: "))

for n in range(for_user_input):
    print("Hello World")

while_user_input = int(input("\nWhile loop, enter a number: "))

while while_user_input > 0:
    print("Hello World")
    while_user_input -= 1

print("\n-----------------------------------------------------------------------------------------------------------\n")

numbers = []

for i in range(3):
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)

if numbers[0] == numbers[1] == numbers[2]:
    print("\nAll numbers are equal")
else:
    print("\nNot all numbers are equal")
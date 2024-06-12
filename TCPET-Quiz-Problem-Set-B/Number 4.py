user_input = int(input("Enter a positive number: "))

if 0 < user_input <= 50:
    for n in range(user_input, 51):
        print(n)
else:
    print("Error")


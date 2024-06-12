user_input = int(input("Enter K: "))

for i in range(user_input):
    text_pattern = '10' * (user_input // 2) + '1' * (user_input % 2)
    print(text_pattern)

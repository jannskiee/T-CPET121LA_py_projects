first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

print("Choose an Operator: ")
print(""""
ADD - Addition
SUB - Subtraction 
MUL - Multiplication
DIV - Division (show separately the remainder)
""")

op_input = str(input("Enter the operator: ")).upper()

if op_input == "ADD":
    result = first_num + second_num
    print(f"Addition Result: {result}")

elif op_input == "SUB":
    result = first_num - second_num
    print(f"Subtraction Result: {result}")

elif op_input == "MUL":
    result = first_num * second_num
    print(f"Multiplication Result: {result}")

elif op_input == "DIV":
    result = first_num / second_num
    remainder_result = first_num % second_num
    print(f"Division Result: {result}")
    print(f"Remainder: {remainder_result}")

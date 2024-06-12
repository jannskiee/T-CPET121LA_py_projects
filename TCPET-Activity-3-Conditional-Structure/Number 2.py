first_name = input("What is the name of the first student: ")
first_prelim = int(input("What is the prelim grade of the first student: "))
first_midterm = int(input("What is the midterm grade of the first student: "))
first_final = int(input("What is the final grade of the first student: "))

second_name = input("\nWhat is the name of the second student: ")
second_prelim = int(input("What is the prelim grade of the second student: "))
second_midterm = int(input("What is the midterm grade of the second student: "))
second_final = int(input("What is the final grade of the second student: "))

first_result = (first_prelim + first_midterm + first_final) / 3
second_result = (second_prelim + second_midterm + second_final) / 3

print(f"\n{first_name} got an average of {first_result}")
print(f"{second_name} got an average of {second_result}")

# a
if first_result >= 60:
    print(f"\n{first_name} passed!")
else:
    print(f"\n{first_name} failed!")

if second_result >= 60:
    print(f"{second_name} passed!")
else:
    print(f"{second_name} failed!")

# b
if first_result == second_result:
    print("\nBoth student have the same average!")
elif first_result > second_result:
    print(f"\n{first_name} got higher average than {second_name}! ")
else:
    print(f"\n{second_name} got higher average than {first_name}!")

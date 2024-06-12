positive = 0
negative = 0
zero = 0

for n in range(5):
    n += 1
    num = int(input("Enter the five numbers values, simultaneously: "))
    if num == 0:
        zero += 1
    elif num > 0:
        positive += 1
    else:
        negative += 1

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")
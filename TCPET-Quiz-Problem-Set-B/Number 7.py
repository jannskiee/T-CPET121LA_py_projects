while True:
    k = int(input("Enter K: "))
    if k <= 10:
        break
    else:
        print("Error! The K should not exceed 10")

for i in range(1, k+1):
    pattern = str(i) * i
    print(pattern)

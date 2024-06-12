start = int(input("Input the start value: "))
key = str(input("Input the key value: ")).upper()

if key == "UP":
    for n in range(start + 1, start + 6):
        print(n)
elif key == "DOWN":
    for n in range(start - 1, start - 6, -1):
        print(n)
else:
    print("Error")

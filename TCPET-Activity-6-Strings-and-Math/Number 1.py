vowels = "aeiouAEIOU"

total_vowels = 0
check = 0

a = str(input("Enter the first string: "))
b = str(input("Enter the second string: "))

total_a = len(a)
total_b = len(b)

print("The total length of first string is: " + str(total_a))
print("The total length of second string is: " + str(total_b))

if total_a > total_b:
    print("The " + a + " string is longer")
    check = 1

elif total_a < total_b:
    print("The " + b + " string is longer")
    check = 0

else:
    print("Both string are same length ")
    check = 2

if check == 1:
    for char in a:
        if char in vowels:
            total_vowels += 1

    print("Total vowels:", total_vowels)

elif check == 0:
    for char in b:
        if char in vowels:
            total_vowels += 1

    print("Total vowels:", total_vowels)

else:
    print("Error both string input, there will be no vowels count check!")

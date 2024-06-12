first_item = int(input("What is the price of the first item: "))
second_item = int(input("What is the price of the second item: "))
third_item = int(input("What is the price of the third item: "))

user_payment = int(input("\nEnter your payment here: "))

total_price = first_item + second_item + third_item

if total_price > 1000:
    print("\nThe total price of the items exceeded 1000, therefore you will get a 10% discount!")
    discount_price = (total_price - (0.10 * total_price))
    if user_payment >= discount_price:
        discount_change = user_payment - discount_price
        print(f"\nYour change is {discount_change} ")
    else:
        print("\nInsufficient Funds")
else:
    print("\nThe total price of the items did not exceeded 1000, therefore you will not get a 10% discount")
    if user_payment >= total_price:
        change = user_payment - total_price
        print(f"\nYour change is {change}")
    else:
        print("\nInsufficient Funds")

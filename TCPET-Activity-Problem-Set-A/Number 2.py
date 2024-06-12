first_input = float(input("Enter the price of the first item: "))
second_input = float(input("Enter the price of the second item: "))
third_input = float(input("Enter the price of the third item: "))

item_total = first_input + second_input + third_input

total_price = 0

if item_total > 5000:
    discounted_price = (item_total - (item_total * .20))
    tax_discounted_price = (item_total * .10)
    print("\nThe total price of the items is greater than 5000, therefore you will get a 20% discount!")
    print(f"Total Price: {discounted_price}")
    print(f"10% Tax from discounted price: {tax_discounted_price}")
    total_price = discounted_price

else:
    print("\nThe total price of the items is not greater than 5000, therefore you will not get a 20% discount")
    print(f"Total Price: {item_total}")
    total_price = item_total

payment_input = float(input("\nEnter your payment here: "))

if payment_input > total_price:
    change = payment_input - total_price
    print("\nThank you for your purchase!")
    print(f"Change: {change}")

elif payment_input == total_price:
    change = payment_input - total_price
    print("\nThank you for giving an exact amount")
    print(f"Change: {change}")

else:
    print("\nInsufficient Funds")
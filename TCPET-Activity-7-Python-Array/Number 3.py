food = {}

name = input("Enter the name of the food: ")
food['Name'] = name

valid_types_input = {'1': 'Appetizer', '2': 'Dessert', '3': 'Main Course'}
type_input = input("Enter the type of the food (1 - Appetizer, 2 - Dessert, 3 - Main Course): ")
food['Type'] = valid_types_input.get(type_input, "Invalid Input!")

valid_tastes_input = {'A': 'Sweet', 'B': 'Sour', 'C': 'Salty', 'D': 'Spicy'}
taste_input = input("Enter the taste of the food (A - Sweet, B - Sour, C - Salty, D - Spicy): ")
food['Taste'] = valid_tastes_input.get(taste_input, "Invalid Input!")

print("FOOD DETAILS --------------------------------------------------------------------------------------------------")
for key, value in food.items():
    print(f"{key}: {value}")

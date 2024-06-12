width_input = int(input("Enter the width of the figure: "))
height_input = int(input("Enter the height of the figure: "))
character_input = input("Enter the character for the figure: ")

for n in range(height_input):
    print(character_input * width_input)

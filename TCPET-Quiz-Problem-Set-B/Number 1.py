START_BOLD_LETTER = "\033[1m"
END_BOLD_LETTER = "\033[0m"

user_input = int(input("Enter the number of days: "))

weeks = user_input // 7
hours = user_input * 24
minutes = hours * 60

print("\n" + START_BOLD_LETTER + "RESULT: " + END_BOLD_LETTER)
print("---------------------------------------------------------------------------------------------------------------")
print(f"{weeks} weeks")
print(f"{hours} hours")
print(f"{minutes} minutes")
print("---------------------------------------------------------------------------------------------------------------")



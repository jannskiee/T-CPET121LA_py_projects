import random

user_bet = int(input("Enter your bet from numbers 1-20: "))

if user_bet < 1 or user_bet > 20:
    print("Error bet number input!")

else:
    random_numbers = [random.randint(1, 20) for _ in range(10)]
    score = random_numbers.count(user_bet)

    print("Numbers:", random_numbers)
    print("Score:", score)

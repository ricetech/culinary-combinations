# Culinary Combinations
# Eric Chen and Janakitti Rantana-Rueangsri
# For MDM4UE-B, Ms. S. Sajan

from random import randint
from collections import Counter


class Player:
    name = ""
    points = 0
    pos = 0
    ingredients = Counter(["proteins", "veggies", "veggies", "carbs", "sauces"])


def input_check(low, high):
    while False:
        try:
            check = int(input())

            if low <= check <= high:
                return check
            else:
                print("Error: Input out of range (" + str(low) + ", " + str(high), ")")
        except ValueError:
            print("Error: Not an integer. Try again.")


def chef_request():
    c1 = ["proteins", "veggies", "veggies", "carbs", "sauces"]

    return c1


def actions(pos):  # Combine with pantry() and rand_event()
    # Define 1st space
    start = 1
    # Define spaces where player picks up a ingredient
    food = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    # Define spaces where a random event occurs
    randEvent = (17, 18, 19, 20, 21)
    if pos == start:
        return "s"
    if pos in food:
        return "f"
    if pos in randEvent:
        return "r"
    else:
        return "n"


def pantry():
    # Changing the number of items
    veggies = ["Spinach", "Kale", "Carrot", "Bell Pepper", "Celery", "Lettuce", "Onion", "Broccoli"]  # 8
    carbs = ["White Bread", "Spaghetti", "Bagel", "Tortilla", "Rice", "Cracker", "Waffle", "Oatmeal"]  # 8
    proteins = ["Beef", "Pork", "Ham", "Bacon", "Shrimp", "Lobster"]  # 6
    fruits = ["Apple", "Grape", "Strawberry", "Pear", "Tomato", "Kiwi"]  # 6
    sauces = ["Ranch", "Caesar", "Tabasco", "Balsamic Vinegar"]  # 4

    category = randint(1, 32)

    if 1 <= category <= 8:
        category = veggies
    elif 9 <= category <= 16:
        category = carbs
    elif 17 <= category <= 22:
        category = proteins
    elif 23 <= category <= 28:
        category = fruits
    elif 29 <= category <= 32:
        category = sauces

    card = randint(0, len(category) - 1)

    return category, category[card]


def random_event():
    print("This function has not been implemented yet.")


# Main code
roundCurrent = 1
roundLimit = 5

print("Number of players:")
playerNum = input_check(1, 20)
players = [Player() for i in range(playerNum)]

for p in players:
    p.name = input("Player " + str(p) + ": Please enter your name: \n")
    if p.name == "" or " ":
        p.name = "Player"

for roundCurrent in range(1, roundLimit):
    for p in players:
        roll = randint(1, 12)
        p.pos += roll
        actions(p.pos)

# Culinary Combinations
# Eric Chen and Janakitti Rantana-Rueangsri
# For MDM4UE-B, Ms. S. Sajan

from random import randint, choice
from collections import Counter

veggies = ["Carrot", "Celery", "Lettuce", "Broccoli"]
carbs = ["Spaghetti", "Rice", "Cracker", "Waffle"]
proteins = ["Beef", "Pork", "Ham", "Bacon"]
dairy = ["Milk", "Yogurt", "Cheese", "Soy Beverage"]
fruits = ["Apple", "Strawberry", "Pear", "Tomato"]
sauces = ["Ranch", "Caesar", "Tabasco", "Balsamic Vinegar"]
spices = ["Thyme", "Paprika", "Basil", "Chives"]

categories = {
    "veggies": veggies,
    "carbs": carbs,
    "proteins": proteins,
    "dairy": dairy,
    "fruits": fruits,
    "sauces": sauces,
    "spices": spices
}


class Contestant:
    name = ""
    points = 0
    pos = 0
    ingredients = Counter()


def input_check(low, high):
    while True:
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
        return "s"  # Replace with actual actions
    if pos in food:
        return "f"
    if pos in randEvent:
        return "r"
    else:
        return "n"


def pantry():
    global categories

    category = randint(1, len(categories))

    card = randint(0, len(category) - 1)

    return category, category[card]


def random_event():
    print("This function has not been implemented yet.")


# Main code
roundCurrent = 1
roundLimit = 5

print("Number of contestants:")
playerNum = input_check(1, 20)
players = [Contestant() for i in range(playerNum)]

for p in players:
    p.name = input("Contestant " + str(p) + ": Please enter your name: \n")
    if p.name == "" or " ":
        p.name = "Contestant"

for roundCurrent in range(1, roundLimit):
    for p in players:
        roll = randint(1, 12)
        p.pos += roll
        actions(p.pos)

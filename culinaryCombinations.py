# Culinary Combinations
# Eric Chen and Janakitti Rantana-Rueangsri
# For MDM4UE-B, Ms. S. Sajan

from random import randint


class Player:
    points = 0
    ingredients = []
    pos = 0

    def __init__(self, name):
        self.name = name


def init():
    c1 = ["proteins", "veggies", "veggies", "carbs", "sauces"]
    c2 = ["proteins"]


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

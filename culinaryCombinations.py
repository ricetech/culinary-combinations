# Culinary Combinations
# This code simulates our proposed board game, which uses combinations, permutations, and probability.
# Eric Chen and Janakitti Rantana-Rueangsri
# For MDM4UE-B, Ms. S. Sajan

from random import randint
from time import sleep
import random

# GAME SETTINGS (predefined constants)
ingredients = (
    "veggies",
    "carbs",
    "proteins",
    "dairy",
    "fruits",
    "sauces",
    "spices",
)

chefRequestTypes = {
    "salad": 4,
    "sandwich": 2,
}

# Target amount of items in combinations
saladIngredients = 4

# Target amount of items in permutations
sandwichIngredients = 2

roundLimit = 5

# Define spaces that give a user an ingredient from their pantry & spaces with random actions
pantryTiles = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23)
actionTiles = (6, 12, 18, 24)

# Other variables that need to be initialized
chefRequest = []

chefRequestType = ""

# Variables for running the game quickly to test probability (AI contestants)
aiContestantCounter = 1
scoreboard = []


class Contestant:
    name = ""
    points = 0
    pointsGained = 0
    pos = 1  # Starting tile
    pantry = []  # Ingredients picked from here
    kitchen = []  # Matching with the chef's request is from here

    def __init__(self):
        global aiContestantCounter
        if speedRun:  # == True
            self.name = "Contestant " + str(aiContestantCounter)
            aiContestantCounter += 1
        else:
            self.name = input("Next contestant, please enter your name: \n")
            if self.name == "" or self.name == " ":
                self.name = "Contestant " + str(aiContestantCounter)
                aiContestantCounter += 1

    def round_start(self):
        self.pantry = list(ingredients)
        self.kitchen = []
        self.pointsGained = 0

    def round_actions(self):
        # Rolling a die
        print("\nIt's " + self.name + "'s turn.")
        if not speedRun:
            input("Press enter to roll the dice.")
            print("Rolling...")
            sleep(1)
        roll = randint(1, 6)
        self.pos += roll
        if self.pos >= (len(pantryTiles) + len(actionTiles)):
            self.pos -= (len(pantryTiles) + len(actionTiles))

        print(self.name, "rolled " + str(roll) + ".")
        if not speedRun:
            sleep(1)

        # Check to see if contestant landed on a particular type of tile (defined at the top of code)
        if self.pos in pantryTiles:
            print(self.name, "landed on tile number", str(self.pos) + ", which is a Pantry Tile.")
            self.pantry_tile()
        elif self.pos in actionTiles:
            print(self.name, "landed on tile number", str(self.pos) + ", which is an Action Tile.")
            action_tile()
        else:
            print(self.name, "landed on tile number", str(self.pos) + ", which is a blank tile.")
        print("-- End of turn --")

    def pantry_tile(self):
        ingredient = random.choice(self.pantry)
        self.kitchen.append(ingredient)
        self.pantry.pop(self.pantry.index(ingredient))
        print("Pantry Tile:", self.name, "got some", ingredient + "!")
        print("New kitchen contents:", self.kitchen)


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
    global chefRequestType
    global chefRequest
    chefRequest = []
    chefRequestType = random.choice(list(chefRequestTypes.keys()))
    for i in range(chefRequestTypes[chefRequestType]):
        chefRequest.append(random.choice(ingredients))


def action_tile():
    print("Error: This function has not been implemented yet.")


def print_scoreboard():
    global scoreboard
    scoreboard = sorted(contestants, key=lambda x: x.points, reverse=True)
    print("SCOREBOARD:\n"
          "Contestant:            Points Added: Points:")
    for s in scoreboard:
        print(("{}...".format(s.name[:23]) if len(s.name) > 22 else s.name).ljust(22) + " "
              + " " + str(s.pointsGained) + "             " + str(s.points))


# Main code
print("Pick one:\n"
      "1: Human Game\n"
      "2: AI Game (instant)")

gameSelector = input_check(1, 2)
if gameSelector == 2:
    speedRun = True
else:
    speedRun = False

while True:
    print("Enter the number of contestants:")
    contestantNum = input_check(1, 20)
    contestants = [Contestant() for cN in range(contestantNum)]

    for roundCurrent in range(1, roundLimit):
        for c in contestants:
            c.round_start()
        print("\nRound " + str(roundCurrent) + ":")
        chef_request()
        print("Chef Request for this round: \n"
              "Type:", chefRequestType, "\n"
              "Contents:", chefRequest)
        for turn in range(chefRequestTypes[chefRequestType]):
            for c in contestants:
                c.round_actions()

        # At the end of the round:
        for c in contestants:
            print(c.name + ":")
            if chefRequestType == "salad":
                for item in chefRequest:
                    if item in c.kitchen:
                        c.pointsGained += 1
                        print("Gained 1 point for matching", item, "to the chef's request.")
            elif chefRequestType == "sandwich":
                for index in range(len(chefRequest)):
                    try:
                        if chefRequest[index] == c.kitchen[index]:
                            c.pointsGained += 1
                            print("Gained 1 point for matching", chefRequest[index], "to the chef's request in position"
                                                                                     , str(index + 1) + ".")
                    except IndexError:
                        continue
            if c.pointsGained == 0:
                print("Did not win any points this round.")
            else:
                print("...for a total of", c.pointsGained, "points won this round.")
            c.points += c.pointsGained

        print_scoreboard()
        print(ingredients)
        print("\n== End of Round ==\n")
    print("WINNER: " + scoreboard[0].name + " with a points of " + str(scoreboard[0].points) + "!")
    print("Play again?\n"
          "1: Yes\n"
          "2: No\n")
    replay = input_check(1, 2)
    if replay == 2:
        raise SystemExit

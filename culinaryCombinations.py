# Culinary Combinations
# This code simulates our proposed board game, which uses combinations, permutations, and probability.
# Eric Chen and Janakitti Rantana-Rueangsri
# For MDM4UE-B, Ms. S. Sajan

from random import randint
from time import sleep
import random

# GAME SETTINGS (predefined constants)
# List of possible ingredients (copied to contestant's pantry and chef request possibilities)
ingredients = (
    "veggies",
    "carbs",
    "proteins",
    "dairy",
    "fruits",
    "sauces",
    "spices",
)

# Dictionary of types of chef requests. The value is the max number of turns in each round when that type is active.
# The value is also the number of ingredients picked.
# IMPROVE: Change into a class or tuple
chefRequestTypes = {
    "salad": 4,
    "sandwich": 2,
}

# Define number of rounds per game
roundLimit = 5

# Define tiles that give a user an ingredient from their pantry & tiles with random actions
pantryTiles = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23)
actionTiles = (6, 12, 18, 24)

# Other variables that need to be initialized (please do not touch)
chefRequest = []

chefRequestType = ""

# Variables for running the game quickly to test probability (AI contestants)
aiContestantCounter = 1
scoreboard = []


class Contestant:
    name = ""  # Display name
    points = 0  # Overall tally of points
    pointsGained = 0  # Points gained in that round (resets every round)
    pos = 1  # Starting tile
    pantry = []  # Ingredients picked from here
    kitchen = []  # Matching with the chef's request is from here

    def __init__(self):
        global aiContestantCounter
        if speedRun:  # == True
            # Automatic creation of names for AI players
            self.name = "Contestant " + str(aiContestantCounter)
            aiContestantCounter += 1
        else:
            self.name = input("Next contestant, please Enter your name: \n")
            # If name is blank, replace with a stock name.
            if self.name == "" or self.name == " ":
                self.name = "Contestant " + str(aiContestantCounter)
                aiContestantCounter += 1

    def round_start(self):
        # Reset the pantry, kitchen, and points gained.
        self.pantry = list(ingredients)
        self.kitchen = []
        self.pointsGained = 0

    def round_actions(self):
        # Rolling a die
        print("\nIt's " + self.name + "'s turn.")
        if not speedRun:
            # Interactive element removed for AI players
            input("Press Enter to roll the dice.")
            print("Rolling...")
            sleep(1)
        roll = randint(1, 6)
        # Add roll to current tile number
        self.pos += roll
        # Used to loop back to tile 1 if contestant goes past tile 24
        if self.pos >= (len(pantryTiles) + len(actionTiles)):
            self.pos -= (len(pantryTiles) + len(actionTiles))

        print(self.name, "rolled " + str(roll) + ".")

        # Time delay (for readability)
        if not speedRun:
            sleep(1)

        # Check to see if contestant landed on a particular type of tile (defined at the top of code)
        if self.pos in pantryTiles:
            print(self.name, "landed on tile number", str(self.pos) + ", which is a Pantry Tile.")
            if not speedRun:
                sleep(1)
            self.pantry_tile()
        elif self.pos in actionTiles:
            print(self.name, "landed on tile number", str(self.pos) + ", which is an Action Tile.")
            action_tile()
        else:
            print(self.name, "landed on tile number", str(self.pos) + ", which is a blank tile.")
        print("-- End of turn --")

        # Time delay for readability
        if not speedRun:
            sleep(2)

    def pantry_tile(self):
        # Pick a random item from the player's pantry
        ingredient = random.choice(self.pantry)
        # Add that item to their kitchen
        self.kitchen.append(ingredient)
        # Remove the item from their pantry (as it got moved to the kitchen)
        self.pantry.pop(self.pantry.index(ingredient))
        print("Pantry Tile:", self.name, "got some", ingredient + "!")
        print("New kitchen contents:", self.kitchen)


def input_check(low, high):
    # This function is to ensure that users do not enter anything except an integer value within a defined range.
    # low is the lower limit of the input range.
    # high is the higher limit of the input range.
    # All inputs must be integers.
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
    # Copy over the list of ingredients defined at the top of the code (temporary storage)
    ingredientBank = list(ingredients)
    # Empty the request from the previous round (if any)
    chefRequest = []
    # Pick a random type of request type (combinations or permutations)
    chefRequestType = random.choice(list(chefRequestTypes.keys()))
    for i in range(chefRequestTypes[chefRequestType]):
        # Pick a random ingredient from the bank
        currentIngredient = random.choice(ingredientBank)
        # Add this ingredient to the request
        chefRequest.append(currentIngredient)
        # Remove this ingredient from the bank (to avoid requests with duplicate ingredients)
        ingredientBank.pop(ingredientBank.index(currentIngredient))


def action_tile():
    print("Error: This function has not been implemented yet.")


def print_scoreboard():
    global scoreboard
    scoreboard = sorted(contestants, key=lambda x: x.points, reverse=True)
    if not speedRun:
        input("Press Enter to continue to the scoreboard.")
    print("\nSCOREBOARD:\n"
          "Contestant:              Points Added: Points:")
    for s in scoreboard:
        # This code creates a table with formatted lines.
        print(("{}...".format(s.name[:20]) if len(s.name) > 20 else s.name).ljust(23) + " "
              + " " + str(s.pointsGained) + "             " + str(s.points))


# Main code
# Choose between human or AI (speedRun) game
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

    # Round counter
    for roundCurrent in range(1, roundLimit):
        # Reset contestant stats (see class Contestant.round_start())
        for c in contestants:
            c.round_start()
        print("\nRound " + str(roundCurrent) + ":")
        # Randomly select a new request for this round
        chef_request()
        print("Chef Request for this round: \n"
              "Type:", chefRequestType, "\n"
              "Contents:", chefRequest)

        if not speedRun:
            input("Press Enter when the all contestants have read the request.\n")
        # Each player gets the number of turns as defined in chefRequestTypes at the top
        for turn in range(chefRequestTypes[chefRequestType]):
            for c in contestants:
                c.round_actions()

        # At the end of the round:
        if not speedRun:
            input("\nEnd of Round. Press Enter to continue to the Round Summary.")
        print("\nROUND SUMMARY:")
        for c in contestants:
            print(c.name + ":")

            # Scorekeeper for combinations
            if chefRequestType == "salad":
                for item in chefRequest:
                    # See if the item in the chef request is anywhere in the contestant's kitchen
                    if item in c.kitchen:
                        c.pointsGained += 1
                        print("Gained 1 point for matching", item, "to the chef's request.")

            # Scorekeeper for permutations
            elif chefRequestType == "sandwich":
                for index in range(len(chefRequest)):
                    try:
                        # See if the item in the chef request is in the same position in the contestant's kitchen
                        if chefRequest[index] == c.kitchen[index]:
                            c.pointsGained += 1
                            print("Gained 1 point for matching", chefRequest[index],
                                  "to the chef's request in position", str(index + 1) + ".")

                    # This error is raised if the item is not found
                    except IndexError:
                        continue

            if c.pointsGained == 0:
                print("Did not win any points this round.")

            # IMPROVEMENT: Add ties
            else:
                print("...for a total of", c.pointsGained, "points won this round.")
            c.points += c.pointsGained

        print_scoreboard()
        print("\n== End of Round ==\n")
        if not speedRun:
            input("Press Enter to continue to the next Round.\n")
    print("WINNER: " + scoreboard[0].name + " with " + str(scoreboard[0].points) + " points!")
    print("\nPlay again?\n"
          "1: Yes\n"
          "2: No\n")
    replay = input_check(1, 2)
    if replay == 2:
        raise SystemExit

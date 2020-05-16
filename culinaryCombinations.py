# Culinary Combinations
# This code simulates our board game, which uses combinations, permutations, and probability.
# Eric C. and Janakitti R.

from random import randint
from time import sleep
import random

# GAME SETTINGS (predefined editable constants)
# List of possible ingredients (copied to Contestant's Pantry and Chef Request possibilities)
ingredients = (
    "veggies",
    "carbs",
    "proteins",
    "dairy",
    "fruits",
    "sauces",
    "spices",
)

# Instantiate all TYPES of Chef Requests.
# One tuple per type.
# Valid categories: "c" (Combinations) or "p" (Permutations)
#
# Syntax and expected types:
# name  = (name, category (see above), maxTurns,     [pointsIndex[0], pointsIndex[1], ... , pointsIndex[n]])
# tuple = (str,  str,                  int,      list[int,            int,            ... , int])
salad = ("Salad", "c", 4, [0, 1, 6, 8, 20])
sandwich = ("Sandwich", "p", 2, [2, 0, 6, 30])

# Instantiate each individual Chef Request.
# One tuple per Request.
# Type is one of the tuples that was defined right above.
#
# Syntax and expected types:
# name  = (name, type (see above),     [item1, item2, item3 [salad only], item4 [salad only]])
# tuple = (str,  tuple,            list[str,   str,   str,                str])

cheesyLychee = ("Cheesy Lychee", salad, ["spices", "carbs", "dairy", "fruits"])
mangoChicken = ("Mango Chicken", salad, ["fruits", "carbs", "proteins", "spices"])
milkyCroutons = ("Milky Croutons", salad, ["spices", "carbs", "dairy", "veggies"])
ramsDeluxe = ("Ram's Deluxe", salad, ["veggies", "proteins", "dairy", "sauces"])
kangarooTail = ("Kangaroo Tail", salad, ["dairy", "carbs", "proteins", "sauces"])
wellnessBowl = ("Wellness Bowl", salad, ["veggies", "spices", "dairy", "sauces"])
farmersShovel = ("Farmer's Shovel", salad, ["veggies", "carbs", "fruits", "proteins"])
italianFire = ("Italian Fire", salad, ["proteins", "veggies", "dairy", "sauces"])
luckyMix = ("Lucky Mix", salad, ["dairy", "spices", "protein", "sauces"])
calamariMayo = ("Calamari Mayo", salad, ["veggies", "sauces", "fruits", "protein"])
spicyGrass = ("Spicy Grass", salad, ["veggies", "carbs", "sauces", "spices"])
megaOrganic = ("Megaorganic", salad, ["veggies", "fruits", "sauces", "spices"])

appleKale = ("Apple Kale", sandwich, ["veggies", "fruits"])
soakedBread = ("Soaked Bread", sandwich, ["spices", "sauces"])
classicStack = ("Classic Stack", sandwich, ["proteins", "veggies"])
northernCrunch = ("Northern Crunch", sandwich, ["dairy", "proteins"])

# Put all of the above Requests into a tuple.
# Type: A tuple that contains tuples.
rawChefRequests = (cheesyLychee, mangoChicken, milkyCroutons, ramsDeluxe, kangarooTail, wellnessBowl, farmersShovel,
                   italianFire, luckyMix, calamariMayo, spicyGrass, megaOrganic, appleKale, soakedBread,
                   classicStack, northernCrunch)

# Define number of Rounds per game
roundLimit = 5

# Define Tile numbers that give a user an ingredient from their Pantry & tiles with random actions
# Numbered in a clockwise loop
pantryTiles = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23)
actionTiles = (6, 12, 18, 24)

# ============
# Extra variables -- DO NOT EDIT ANYTHING BELOW HERE --
# ============
chefRequest = None  # Storage for current Chef Request
chefRequests = []  # Storage for Chef Request objects that are created later

# Variables for running the game quickly to test probability (AI contestants)
aiContestantCounter = 1

# Scoreboard (points counter)
scoreboard = []
winners = []


class ChefRequest:
    name = ""  # Display Name
    type = ""  # Display Type
    category = ""  # Request category, 'c' or 'p' (Combinations/Permutations) for scoring purposes
    maxTurns = 0  # Max turns allowed
    pointsIndex = []  # Number of matches (index #) and number of points awarded (item)
    contents = []

    def __init__(self, data):
        self.name = data[0]
        # This syntax accesses the 1st item of the 2nd item of data (since item 2 of data is a nested tuple)
        self.type = data[1][0]
        self.category = data[1][1]
        self.maxTurns = data[1][2]
        self.pointsIndex = data[1][3]
        self.contents = data[2]


class Contestant:
    name = ""  # Display name
    points = 0  # Overall tally of points
    matches = 0  # Number of matches in current Round
    pointsGained = 0  # Points gained in that Round (resets every Round)
    pos = 1  # Starting Tile
    Pantry = []  # Ingredients picked from here
    kitchen = []  # Matching with the Chef's Request is from here

    def __init__(self):
        global aiContestantCounter
        if speedRun:  # Equivalent of if speedRun == True
            # Automatic creation of names for AI players
            self.name = "Contestant " + str(aiContestantCounter)
            aiContestantCounter += 1
        else:
            self.name = input("Next Contestant, please Enter your name: \n")
            # If name is blank, replace with a stock name.
            if self.name == "" or self.name == " ":
                self.name = "Contestant " + str(aiContestantCounter)
                aiContestantCounter += 1

    def round_start(self):
        # Reset the Pantry, Kitchen, and points gained.
        self.Pantry = list(ingredients)
        self.kitchen = []
        self.matches = 0
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
        # Add roll to current Tile number
        self.pos += roll
        # Used to loop back to Tile 1 if Contestant goes past the last Tile on the board
        if self.pos >= (len(pantryTiles) + len(actionTiles)):
            self.pos -= (len(pantryTiles) + len(actionTiles))

        print(self.name, "rolled " + str(roll) + ".")

        # Time delay (for readability)
        if not speedRun:
            sleep(1)

        # Check to see if Contestant landed on a particular type of Tile (defined at the top of code)
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
        # Pick a random item from the Contestant's Pantry
        ingredient = random.choice(self.Pantry)
        # Add that item to their Kitchen
        self.kitchen.append(ingredient)
        # Remove the item from their Pantry (because it got moved to the Kitchen)
        self.Pantry.pop(self.Pantry.index(ingredient))
        print("Pantry Tile:", self.name, "got some", ingredient + "!")
        print("New kitchen contents:", self.kitchen)


def input_check(low, high):
    """
    This function is to ensure that users do not enter anything except an integer value within a defined range.

    Keyword Arguments:
    low --  the lower limit of the input range.
    high -- the higher limit of the input range.
    All inputs must be integers.
    Another helpful function is the protection against a program crash if the user happens to enter anything
    other than an integer.
    """
    while True:
        try:
            check = int(input())

            if low <= check <= high:
                return check
            else:
                print("Error: Input out of range (" + str(low) + ", " + str(high), ")")
        # Prevent a program crash if something other than an integer is inputted
        except ValueError:
            print("Error: Not an integer. Try again.")


def chef_request():
    # Intake the chefRequest variable from outside of the function
    global chefRequest
    # Empty the Request from the previous Round (if any)
    chefRequest = None
    # Pick a random Request
    chefRequest = random.choice(chefRequests)


def action_tile():
    print("Action tiles do not have a calculable outcome, and are therefore excluded from this simulation.")


def print_scoreboard():
    global scoreboard
    # 1. Copy the list of contestants into scoreboard (so turn order isn't affected)
    # 2. Sort the contestants by points from greatest to least
    scoreboard = sorted(contestants, key=lambda x: x.points, reverse=True)
    if not speedRun:
        input("Press Enter to continue to the scoreboard.")
    print("\nSCOREBOARD:\n"
          "Contestant:              Points Gained: Points:")
    for s in scoreboard:
        # This code creates a table with formatted lines.
        if s.pointsGained < 10:
            pointsGained = str(s.pointsGained) + " "
        else:
            pointsGained = s.pointsGained

        print(("{}...".format(s.name[:20]) if len(s.name) > 20 else s.name).ljust(23) + " "
              + " " + str(pointsGained) + "             " + str(s.points))


# Main code

# Create all of the Chef Requests based on the tuples at the top of the code
for cR in rawChefRequests:
    newCR = ChefRequest(cR)
    chefRequests.append(newCR)

# Choose between human or AI (speedRun) game
print("Pick one:\n"
      "1: Human Game\n"
      "2: AI Game (instant)")

gameSelector = input_check(1, 2)
# speedRun is used throughout the code to skip anything requiring a human input, and automate it to speed up
# the game.
if gameSelector == 2:
    speedRun = True
else:
    speedRun = False

while True:
    print("Enter the number of contestants:")
    contestantNum = input_check(1, 20)
    # Create a Contestant object for each Contestant.
    contestants = [Contestant() for cN in range(contestantNum)]

    # Round counter
    for roundCurrent in range(roundLimit):
        # Reset Contestant stats (see the class method Contestant.round_start())
        for c in contestants:
            c.round_start()
        print("\nRound " + str(roundCurrent) + ":")

        # Randomly select and display a new Request for this Round
        chef_request()
        print("Chef Request for this round: " + chefRequest.name + "\n"
              "Type:", chefRequest.type, "\n"
              "Contents:", chefRequest.contents)

        if not speedRun:
            input("Press Enter when the all contestants have read the request.\n")

        # Each Contestant gets the number of turns as defined in ChefRequest.maxTurns at the top
        for turn in range(chefRequest.maxTurns):
            for c in contestants:
                c.round_actions()

        # At the end of the Round:
        if not speedRun:
            input("\nEnd of Round. Press Enter to continue to the Round Summary.")
        print("\nROUND SUMMARY:")
        for c in contestants:
            print("\n" + c.name + ":")

            # Scorekeeper for combinations
            if chefRequest.category == "c":
                for item in chefRequest.contents:
                    # See if the item in the Chef Request is anywhere in the Contestant's Kitchen
                    if item in c.kitchen:
                        c.matches += 1
                        print("Matched", item, "to the chef's request.")

            # Scorekeeper for permutations
            elif chefRequest.category == "p":
                for index in range(len(chefRequest.contents)):
                    try:
                        # See if the item in the Chef Request is in the same position in the Contestant's Kitchen
                        if chefRequest.contents[index] == c.kitchen[index]:
                            c.matches += 1
                            print("Matched", chefRequest.contents[index],
                                  "to the chef's request in position", str(index + 1) + ".")

                    # Catch allows code to continue if there is no match.
                    except IndexError:
                        continue

            # Record the Contestant's points gained for this Round to display on the scoreboard.
            c.pointsGained = chefRequest.pointsIndex[c.matches]
            # Add the Contestant's points from this Round to their overall score.
            c.points += c.pointsGained
            if c.pointsGained == 0:
                print("Did not win any points this round.")
            else:
                print(c.name, "had a total of", c.matches, "match(es) and gained",
                      c.pointsGained, "point(s) this round.")
        # IMPROVEMENT: ADD BONUSES

        # Display the scoreboard.
        print_scoreboard()
        print("\n== End of Round ==\n")
        if not speedRun:
            input("Press Enter to continue to the next Round.\n")

    # If there's only 1 Contestant, or the 1st place Contestant on the scoreboard has more points than 2nd place
    if len(scoreboard) == 1 or scoreboard[0].points != scoreboard[1].points:
        # ...then display them as the winner.
        print("WINNER: " + scoreboard[0].name + " with " + str(scoreboard[0].points) + " points!")

    else:  # In case of a tie
        # Take the highest score to use as a comparison
        highestScore = scoreboard[0].points
        for c in scoreboard:
            # For each person on the scoreboard, if their score equals that of the person with the highest score...
            if c.points == highestScore:
                # ...add them to the list of winners.
                winners.append(c)
        print("WINNERS: It's a TIE between:")
        for c in winners:
            print(c.name)
        print("...who all had", highestScore, "points!")

    print("\nPlay again?\n"
          "1: Yes\n"
          "2: No\n")
    replay = input_check(1, 2)
    if replay == 2:
        raise SystemExit

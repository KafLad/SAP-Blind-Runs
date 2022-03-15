########################################################################################
#   Super Auto Pets - Blind Computer Player Project                                    #
#                                                                                      #
#   File: SAP.py                                                                       #
#                                                                                      #
#   Written By: Ethan Gray                                                             #
#   Copyright 2022, Ethan Gray, All Rights Reserved                                    #
#                                                                                      #
#   About: A simple, primitive, blind, computer randomizer that plays Super Auto Pets. #
#          Granted, it plays it quite poorly, but it plays it!                         #
########################################################################################


###############
#   IMPORTS   #
###############

import pyautogui as pa
import time
import random as r


#################
#    GLOBAL     #
#   VARIABLES   #
#################

# Global Variables -- These are altered by the specific screen setup [ATM is hard-coded to the 2 setups I have, but planned to be dynamically updated]
tChoices = []
bChoices = []
endTurn = []
pets = []
petShopInit = []
petShopAdd1 = []
foodShopInit = []
foodShopAdd1 = []
rollCoord = []
freezeCoord = []
excessGoldCoord = []
sellCoords = []
petCount = 0


###################
#    FUNCTIONS   #
##################

def ResolutionSetup():
    """
        Ask the user for their resolution size. As of V1.1, the program is only designed for the 2 setups I have (laptop and desktop).
        Planned to work dynamically with a GUI once the program is functional. 
    """


    print("Choose which screensize you currently have")
    size = int(input("(1920x1080 = 1 | Framework Laptop = 2): "))
    valids = [1, 2]

    while size not in valids:
        size = int(input("(1920x1080 = 1 | Framework Laptop = 2): "))


    # Screen Variables
    if size == 1:
        print("You have a 1080p screen!")
        HDPosSetup()
    elif size == 2:
        print("You have a Framework Laptop screen!")
        FWPosSetup()


def HDPosSetup():
    """
        Updates the global variables for the desktop monitor setup
    """
    global tChoices, bChoices, endTurn, pets, petShopInit, petShopAdd1, petShopAdd2, foodShopInit, foodShopAdd1, rollCoord, freezeCoord, excessGoldCoord, sellCoords

    # Main UI Initialization
    tChoices = [ [504, 965], [1122, 945], [1648, 953] ]
    bChoices = [ [384, 1244], [1053, 1233], [1618, 1228] ]
    endTurn = [ 1653, 1538 ]
    pets = [ [508, 973] , [672, 960], [852, 945], [990, 942], [1073, 944] ]
    rollCoord = [ 247, 1513 ]
    freezeCoord = [ 1103, 1568] 
    excessGoldCoord = [ 1237, 1228 ]
    sellCoords = freezeCoord


    # Shop UI Initialization [Including shop scaling for later]
    petShopInit = [ [541, 1239] , [674, 1222] , [817, 1226] ]
    petShopAdd1 =  [977, 1219]
    petShopAdd2 = [1115, 1227]
    foodShopInit =  [ [1403, 1248] ]
    foodShopAdd1 =   [1259, 1261 ]


def FWPosSetup():
    """
        Updates the global variables for the laptop setup.
    """


    global tChoices, bChoices, endTurn, pets, petShopInit, petShopAdd1, petShopAdd2, foodShopInit, foodShopAdd1, rollCoord, freezeCoord, excessGoldCoord, sellCoords

    # Main UI Initialization
    tChoices = [ [498, 601], [1143, 575], [1906, 585] ]
    bChoices = [ [540, 961], [1160, 923], [1817, 949] ]
    endTurn = [ 1983, 1291 ]
    pets = [ [1265, 624] , [1128, 632], [951, 625], [800, 632], [618, 631] ]
    rollCoord = [300, 1290]
    freezeCoord = [1245, 1275] 
    excessGoldCoord = [ 1509, 899 ]
    sellCoords = freezeCoord 


    # Shop UI Initialization [Including shop scaling for later]
    petShopInit = [ [620, 965] , [801, 953] , [958, 955] ]
    petShopAdd1 =  [1111, 944]
    petShopAdd2 = [1330, 932]
    foodShopInit =  [ [1636, 958] ]
    foodShopAdd1 =   [1463, 925]


def TeamName():
    """
        Has the computer randomly choose a team name for the game.
        [Uses the tChoices and bChoices global position variables to know where it needs to go.]
    """


    global tChoices, bChoices

    topChoices = tChoices
    botChoices =  bChoices
    top = r.randint(0,len(topChoices) - 1)
    bot = r.randint(0,len(botChoices) - 1)
    pa.moveTo(topChoices[top][0], topChoices[top][1])
    pa.click()
    pa.moveTo(botChoices[bot][0], botChoices[bot][1])
    pa.click()
    pa.moveTo(endTurn[0], endTurn[1])
    pa.click()


def Shuffle(numShuffles):
    """
        Randomly shuffles the team and then ends the turn.
    """


    global pets, excessGoldCoord


    coords =  pets
    for i in range(numShuffles):
        op1 = r.randint(0, len(coords) - 1)
        op2 = r.randint(0, len(coords) - 1)
        while op2 == op1:
            op2 = r.randint(0, len(coords) - 1)
        pos1 = coords[op1]
        pos2 = coords[op2]
        pa.moveTo(pos1[0], pos1[1])
        pa.click()
        pa.moveTo(pos2[0], pos2[1])
        pa.click()
    pa.moveTo(endTurn[0],endTurn[1])
    time.sleep(1)
    pa.click()
    pa.moveTo(excessGoldCoord[0], excessGoldCoord[1])
    time.sleep(0.5)
    pa.click()


def ShopTime(turn):
    """
        Decides what items to buy, dynamically updates the shop coordinates with when the game updates the shop.
        [In time, this function will be split up into several smaller functions to make sure things are easier to read.]
    """


    global petShopInit, petShopAdd1, petShopAdd2, pets, foodShopInit, foodShopAdd1, petCount, freezeCoord

    # Coordinate Updating & Variable Initialization

    petCoords =  petShopInit
    foodCoords =  foodShopInit
    if turn >= 3:
        foodCoords.append( foodShopAdd1 )
    if turn >= 5:
        petCoords.append( petShopAdd1 )
    if turn >= 9:
        petCoords.append( petShopAdd2 )
    coords = pets
    gold = 10

    # Actual loop
    while gold > 0:
        time.sleep(0.1)
        if turn != 1:
            purchaseType = r.randint(0,2)
        else:
                purchaseType = 1

    
        if purchaseType == 0:
            # Roll
            print("Rolling . . .")
            pa.moveTo(rollCoord[0], rollCoord[1])
            pa.click()
            time.sleep(0.75)
            gold -= 1
    
        elif purchaseType == 1:
            # Pet
            if petCount == 5:
                print("Selling Pet . . .")
                petSell = r.randint(0, len(coords) - 1)
                pa.moveTo(coords[petSell][0], coords[petSell][1])
                pa.click()
                time.sleep(0.15)
                pa.moveTo(freezeCoord[0], freezeCoord[1])
                pa.click()
                gold += 1
                petCount -= 1
            
            time.sleep(1)
            print("Buying Pet . . .")
            pet = r.randint(0, len(petCoords) - 1)
            pa.moveTo(petCoords[pet][0], petCoords[pet][1])
            pa.click()
            teamSlot = r.randint(0, len(coords) - 1)
            time.sleep(0.5)
            pa.moveTo(coords[teamSlot][0], coords[teamSlot][1])
            pa.click()
            gold -= 3
            petCount += 1

        else:
            # Food
            print("Buying Food . . .")
            fud = r.randint(0,len(foodCoords) - 1)
            pa.moveTo(foodCoords[fud][0], foodCoords[fud][1])
            pa.click()
            teamSlot = r.randint(0, len(coords) - 1)
            time.sleep(0.5)
            pa.moveTo(coords[teamSlot][0], coords[teamSlot][1])
            pa.click()
            gold -= 3

           


#############
#   MAIN    #
#   LOOP    #
#############

if __name__ == "__main__":
    ResolutionSetup()
    time.sleep(1)
    turn = 1

    while turn < 100:
        print(f"\nBeginning Turn {turn}!\n")
        time.sleep(0.25)
        ShopTime(turn)
        shuffling = 5
        Shuffle(shuffling)
        time.sleep(5)
        if turn == 1:
            TeamName()
        pa.moveTo(excessGoldCoord)
        pa.click()


        for i in range(30):
            time.sleep(2)
            pa.moveTo(excessGoldCoord)
            pa.click()

        turn += 1
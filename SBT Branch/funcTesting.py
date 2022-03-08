##############################
#   SmartBot Testing Branch  #
#   For use with the 2nd     #
#       branch ONLY          #
##############################


import pyautogui as pa
import time


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
currSlots = {0: False, 1: False, 2: False, 3: False, 4: False}



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




## Redo of the shop functions, just to test and see if I can make a better and easier-to-read version

def SmartShop():
    time.sleep(5)
    
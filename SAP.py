import pyautogui as pa
import time
import random as r



def TeamName():
    topChoices = [ [498, 601], [1143, 575], [1906, 585] ]
    botChoices = [ [540, 961], [1160, 923], [1817, 949] ]
    top = r.randint(0,len(topChoices) - 1)
    bot = r.randint(0,len(botChoices) - 1)
    pa.moveTo(topChoices[top][0], topChoices[top][1])
    pa.click()
    pa.moveTo(botChoices[bot][0], botChoices[bot][1])
    pa.click()
    pa.moveTo(1983, 1291)
    pa.click()


def GetLocation():
    # In theory, can have the user press a key and it will record where the mouse is and write down those coords
    while True:
        time.sleep(0.5)
        print(pa.position())

def Shuffle(numShuffles):
    coords = [ [1265, 624] , [1128, 632], [951, 625], [800, 632], [618, 631] ]
    for i in range(numShuffles):
        op1 = r.randint(0, len(coords) - 1)
        op2 = r.randint(0, len(coords) - 1)
        while op2 == op1:
            op2 = r.randint(0, len(coords) - 1)
        pos1 = coords[op1]
        pos2 = coords[op2]
        pa.moveTo(pos1[0], pos1[1])
        pa.click()
        #time.sleep(0.15)
        pa.moveTo(pos2[0], pos2[1])
        pa.click()
    pa.moveTo(1983,1291)
    pa.click()


def ShopTime(turn):
    # Coordinate Updating & Variable Initialization

    petCoords = [ [620, 965] , [801, 953] , [958, 955] ]
    foodCoords = [ [1636, 958] ]
    if turn >= 3:
        foodCoords.append( [1463, 925] )
    if turn >= 5:
        petCoords.append( [1111, 944] )
    if turn >= 9:
        petCoords.append( [1330, 932] )
    coords = [ [1265, 624] , [1128, 632], [951, 625], [800, 632], [618, 631] ]
    gold = 10

    # Actual loop

    purchaseType = r.randint(0,2)
    if purchaseType == 0:
        # Roll
        print("Rolling . . .")
        pa.moveTo(300, 1290)
        pa.click()
    elif purchaseType == 1:
        # Pet
        print("Buying Pet . . .")
        pet = r.randint(0, len(petCoords) - 1)
        pa.moveTo(petCoords[pet][0], petCoords[pet][1])
        
    else:
        # Food
        print("Buying Food . . .")



if __name__ == "__main__":
    time.sleep(1)
    shuffling = r.randint(10,20)
    # Shuffle(shuffling)
    # time.sleep(5)
    # TeamName()
    GetLocation()

# Slot 1: (x=1265, y=624)
# Slot 2: (x=1128, y=632)
# Slot 3: (x=951, y=625)
# Slot 4: (x=800, y=632)
# Slot 5: (x=618, y=631)
# End Turn: (x=1983, y=1291)
# End w/ Excess: (x=1509, y=899)
# Roll: (x=300, y=1290)
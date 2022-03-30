# TODO:
#   * Work on a JSON file that the program will read thru
#   * Make a function called ConfidenceCalc() that runs in __init__
#       * This will set the confidence value for each pet on startup and use that data for the round, it will then update the JSON values afterwards 
#   * Hook up the JSON file to the Buy() function that way it can be tested

import pyautogui as pag
import random as rand

class Logic:
    topNames = [[118, 242] , [333, 255], [750, 247]]
    botNames = [[97, 396], [414, 408], [660, 407]]
    turn = 1
    health = 10
    coins = 10

    def __init__(self):
        print("Logic Unit Initiated!")

    def Buy(self, shopCoords, shopPets, teamCoords, teamNames):
        # TODO: For loop that reads the file of pet stats and puts confidence value into list
        # altNames = teamNames
        # altCoords = teamCoords
        # for i in range(len(teamCoords), 0, -1):
        #     if teamNames[i] == 'Rock':
        #         teamCoords.pop(i)
        #         teamNames.pop(i)
        #         pass
        # After this loop above, will want to put the file reading. Then after file reading, make teamNames = altNames and teamCoords = altCoords
       
        for i in range(0, len(shopPets)):
            ## Curiosity is commented out for now, will implement it once the file is complete and is being parsed
            # curiosity = rand.randint(0, 100)
            # if curiosity > 15 and curiosity < 25:
            #     # Will eventually make it so even tho it is below specific threshold of confidence, it will randomly choose to buy that pet
            #     i += 1
            i += 1            
            # This loop is relatively pointless for now, but will be useful later to filter out which items in the shop the bot will consider to buy

        
# TODO:
#   * Work on a JSON file that the program will read thru
#   * Make a function called ConfidenceCalc() that runs in __init__
#       * This will set the confidence value for each pet on startup and use that data for the round, it will then update the JSON values afterwards 
#   * Hook up the JSON file to the Buy() function that way it can be tested
import math
import pyautogui as pag
import random as rand
import json

class Logic:
    topNames = [[118, 242] , [333, 255], [750, 247]]
    botNames = [[97, 396], [414, 408], [660, 407]]
    currentTeam = []
    turn = 1
    health = 10
    coins = 10
    petKeys = []
    petData = []
    petDict = {}
    confidenceVals = []

    def __init__(self):
        self.LoadStats()
        self.CalculateConfidence()
        print("Logic Unit Initiated!")


    def LoadStats(self):
        f = open('SBT Branch\\.stats.json')
        data = json.load(f)
        for i in data['Pets']:
            self.petKeys.append(i)
        for i in range(0, len(self.petKeys)):
            self.petData.append(data['Pets'][self.petKeys[i]])

        
    
    def CalculateConfidence(self):
        for i in range(len(self.petKeys)):
            bought = self.petData[i][0]['times_bought']
            roundWins = self.petData[i][0]['rounds_won']
            roundLoss = self.petData[i][0]['rounds_lost']
            gameWins = self.petData[i][0]['games_won']

            b = bought % 3
            if b == 0:
                b = bought / 3
            r = roundWins % 5
            if r == 0:
                r = roundWins / 5
            l = roundLoss % 10
            if l == 0:
                l = roundLoss / 10
            g = gameWins * 10

            confidence = float(((b + r + g) - l)/ 100)
            self.confidenceVals.append(confidence)
        
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

    def UpdateStats(self, result):
        if result == 'Victory':
            for i in range(len(self.currentTeam)):
                print("E")
if __name__ == "__main__":
    logi = Logic()
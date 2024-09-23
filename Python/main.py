from messages import*
import random

game = True
possibleNumber = 0
turnsCount = 0

minNumber = -1
maxNumber = 101

myNumber = random.randint(0, 100)

#Functions

def inputAnalysisGameRegime_1(number):
        global minNumber, maxNumber, game

        playerResponse = input()
        while game:
                if playerResponse.lower() == "б":
                        minNumber = number + 1
                        break
                        
                elif playerResponse.lower() == "м":
                        maxNumber = number - 1
                        break

                elif playerResponse.lower() == "так":
                        win()
                        break
                
                else:
                        commandCall(playerResponse)
                        if game: playerResponse = input()


def inputAnalysisGameRegime_2(num, targetNum):
        if num < targetNum:
                print("Ні, моє число більше!")
                
        elif num > targetNum:
                print("Ні, моє число менше!")

        else:
                print("Так, це моє число!")
                win()

def commandCall(command):
        global game, filename, exitCommand, invalidInputMessage, rulesMessage, rulesCommand
        
        if command == filename:
                print(filename)
                
        elif command.lower() == exitCommand:
                game = False
                
        elif command == rulesCommand:
                print(rulesMessage)
                
        else:
                print(invalidInputMessage)

def win():
        global gameRegime, turnsCount, minNumber, maxNumber, myNumber

        if gameRegime == "1":
                print(programWinMessage + str(turnsCount))
                minNumber = -1
                maxNumber = 101

        else:
                print(playerWinMessage + str(turnsCount))
                myNumber = random.randint(0, 100)
                
        turnsCount = 0
        print("Зараз ви можете обрати інший режим гри, чи продовжити гру в тому самому. Оберіть 1, 2 або вихід")
        gameRegime = input()
        
#Game

print(greetingsMessage)
gameRegime = input()     

while game:
        if gameRegime == "1":
                
                if minNumber != maxNumber and minNumber < maxNumber:
                        turnsCount += 1
                        possibleNumber = random.randint(minNumber, maxNumber)
                        print(possibleNumberMessage + str(possibleNumber) + " ?")
                        inputAnalysisGameRegime_1(possibleNumber)
                
                else:
                        print("Згідно ваших попередніх відповідей, ваше число: " + str(maxNumber))
                        win()
        
        elif gameRegime == "2":
                playerGuess = input()
                
                if playerGuess.isdigit():
                        inputAnalysisGameRegime_2(int(playerGuess), myNumber)
                        turnsCount += 1
                
                else:
                        commandCall(playerGuess)
        
        else:
                commandCall(gameRegime)
                if game: gameRegime = input()

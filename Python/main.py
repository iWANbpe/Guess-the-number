from messages import*
import random

game = True
possibleNumber = 0
turnsCount = 0

minNumber = -1
maxNumber = 101

myNumber = random.randint(0, 100)

print(greetingsMessage)
gameRegime = input()     

if gameRegime == "1":
        print(rules1)
elif gameRegime == "2":
        print(rules2)

def inputAnalysisGameRegime_1(number):
        global minNumber, maxNumber, game

        playerResponse = input()
        while True:
                if playerResponse.lower() == "б":
                        minNumber = number
                        break
                        
                elif playerResponse.lower() == "м":
                        maxNumber = number
                        break

                elif playerResponse.lower() == "так":
                        win()
                        break
                
                elif playerResponse == filename:
                        print(filename)
                        playerResponse = input()

                elif playerResponse.lower() == exitCommand:
                        game = False
                        break
                else:
                        print(invalidInputMessage)
                        playerResponse = input()

        if(minNumber == maxNumber):
                print("Згідно ваших попередніх відповідей, ваше число: " + str(maxNumber))
                win()

def inputAnalysisGameRegime_2(num, targetNum):
        if num < targetNum:
                print("Ні, моє число більше!")
                
        elif num > targetNum:
                print("Ні, моє число менше!")

        else:
                print("Так, це моє число!")
                win()

def win():
        global gameRegime, turnsCount

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

        if gameRegime == "1":
                print(rules1)
        elif gameRegime == "2":
                print(rules2)

while game:
        
        if gameRegime == "1":
                possibleNumber = random.randint(minNumber + 1, maxNumber - 1)
                print(possibleNumberMessage + str(possibleNumber) + " ?")

                inputAnalysisGameRegime_1(possibleNumber)
                turnsCount += 1

        elif gameRegime == "2":
                playerGuess = input()
                
                if playerGuess.isdigit():
                        inputAnalysisGameRegime_2(int(playerGuess), myNumber)
                        turnsCount += 1
                
                elif playerGuess == filename:
                        print(filename)

                elif playerGuess.lower() == exitCommand:
                        game = False
                
                else:
                        print(invalidInputMessage)

        elif gameRegime == filename:
                print(filename)
                gameRegime = input()

        elif gameRegime == exitCommand:
                game = False

        else:
                print(invalidInputMessage)
                gameRegime = input()

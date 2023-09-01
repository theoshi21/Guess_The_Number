from random import randint

def play():
    while True:
        ask = input("Do you want to play? [Yes/No]: ")
        asked = ask.lower()

        if asked == "yes" or asked == "y":
            return True
        elif asked == "no" or asked =="n":
            return False
        else:
            print("Invalid answer, try again.")

def split(num):
    intoString = str(num)
    return list(intoString)

def isHighLow(sysNum,userNum):
    if userNum > sysNum:
        return print("The number is lower")
    elif userNum < sysNum:
        return print("The number is higher.")

def sameCounter(sysNum,userNum):
    counter = 0
    for x in enumerate(sysNum):
        for y in enumerate(userNum):
            if x == y:
                counter += 1
    return print(f"You have guessed {counter} number.")

def startGTN():
    NumToGuess = randint(10000,99999)
    while(True):
        userGuess = input("Enter a number from 10000 - 99999: ")
        if int(userGuess) == NumToGuess:
            print(f"Congrats, you guessed the number! ({NumToGuess})")
            break
        elif userGuess != NumToGuess and userGuess.isnumeric():
            isHighLow(int(NumToGuess),int(userGuess))
            sameCounter(split(NumToGuess),split(userGuess))
            print()
        else: print("Invalid answer, try again.")




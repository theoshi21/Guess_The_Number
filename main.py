from stopwatch import startTime, stopTime, convertTime
from game import startGTN, play

print("-*-*- Guess The Number -*-*-")

gameState = play()

while(gameState):
    start = startTime()
    startGTN()
    finish = stopTime(start)
    convert = convertTime(finish)
    print(f"TIME: {convert}s")
    print()
    gameState = play()

print("Thank you for playing.")
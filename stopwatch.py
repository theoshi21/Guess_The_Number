import time

def startTime():
    start = time.time()
    return start

def stopTime(start):
    finish = time.time() - int(start)
    return finish

def convertTime(finish):
    sec = int(finish) % 60
    minute = int(finish/60) % 60
    converted = f"00:{minute:02}:{sec:02}"
    return converted




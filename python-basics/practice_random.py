import random

# https://pythonbasics.org/random-numbers/

def oneRand():
    x = random.random()

def printThreeRand():
    x = random.random()
    y = random.random()
    z = random.random()
    print(x, y, z)

def avgHundredRands():
    total = 0
    for i in range(100):
        total += random.randrange(0, 10)
    avg = total / 100
    print("Average:", avg)

def main():
    oneRand()
    printThreeRand()
    avgHundredRands()

main()
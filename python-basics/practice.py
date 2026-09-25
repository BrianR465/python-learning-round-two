# https://pythonbasics.org/execute-python-scripts/

def name():
    print("My name is Brian")

def annoyingSong():
    print("I know a song that gets on everybody's nerves")
    print("Everybody's nerves")
    print("Everybody's nerves")
    print("I know a song that gets on everybody's nerves")
    print("And this is how it goes...")

#https://pythonbasics.org/variables/
def printNums():
    num1 = 10 
    num2 = 4.4
    num3 = 3.14159
    print("Integer: ", num1)
    print("Float: ", num2)
    print("Pi: ", num3)

def add():
    print("64 + 32 =", 64 + 32)

def addTwoNums(x,y):
    print(x, "+", y, "=", x+y)

# https://pythonbasics.org/strings/
def actorName():
    print("Bryan Cranston")

def lucky():
    # alternative method of combining numbers and text
    s = "My lucky number is " + str(7) + ", what is yours?"
    print(s)
    print(s[3:8])

def main():
    # name()
    # annoyingSong()
    # printNums()
    # add()
    # addTwoNums(30, 100)
    # actorName()
    # lucky()

    print("End of main func")

main()
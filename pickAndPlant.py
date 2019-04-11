import random

#initializing board of 5x5
array = [["[&]","[ ]","[ ]","[*]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]","[ ]","[ ]"]]
kangaRow = 0
kangaCol = 0
cardinal = 1
canPlace = False

#flowerRow = random.randint(0,4)
#flowerColumn = random.randint(0,4)

#array[flowerRow][flowerColumn] = "[*]"

def main():
    printBoard()
    hop()
    hop()
    hop()
    pick()
    turnRight()
    hop()
    hop()
    place()
    turnLeft()
    hop()
    
def hop():
    global kangaRow
    global kangaCol
    global cardinal
    prevRow = kangaRow
    prevCol = kangaCol
    if (cardinal == 0):
        kangaRow-=1
    elif (cardinal == 1):
        kangaCol+=1
    elif (cardinal == 2):
        kangaRow+=1
    else:
        kangaCol-=1
    if (kangaRow > 4 or kangaCol > 4 or kangaRow < 0 or kangaCol < 0):
        print("The kangaroo is on the edge of the garden, cannot hop any further!")
        kangaRow = prevRow
        kangaCol = prevCol
    else:
        if (array[kangaRow][kangaCol] == "[*]"):
            array[prevRow][prevCol] = "[ ]"
            array[kangaRow][kangaCol] = "[&/*]"
        elif (array[prevRow][prevCol] == "[&/*]"):
            array[prevRow][prevCol] = "[*]"
            array[kangaRow][kangaCol] = "[&]"
        else:
            array[prevRow][prevCol] = "[ ]"
            array[kangaRow][kangaCol] = "[&]"
        printBoard()

def turnLeft():
    global cardinal
    if (cardinal == 0):
        cardinal = 3
    elif (cardinal == 1):
        cardinal = 0
    elif (cardinal == 2):
        cardinal = 1
    else:
        cardinal = 2

def turnRight():
    global cardinal
    if (cardinal == 0):
        cardinal = 1
    elif (cardinal == 1):
        cardinal = 2
    elif (cardinal == 2):
        cardinal = 3
    else:
        cardinal = 0
        
def pick():
    global canPlace
    if (array[kangaRow][kangaCol] != "[&/*]"):
        print("There is nothing to pick here!")
    else:
        array[kangaRow][kangaCol] = "[&]"
        canPlace = True
        printBoard()
        
def place():
    global canPlace
    if (canPlace == True):
        array[kangaRow][kangaCol] = "[&/*]"
        canPlace = False
    else:
        print("You have nothing to place!")
    printBoard()

def printBoard():
    for subarray in array:
        print(subarray)
    print()
        
main()
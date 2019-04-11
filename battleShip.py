import random
import numpy

#playing 4 games
for i in range(4):
    print("Game " + str(i + 1) + "\n")
    #initializing board at 5 rows and 5 columns
    array = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
    
    #printing the blank board
    for subarray in array:
        print(subarray)
    
    print()
    
    #getting the coordinates for computer ship
    randomRow = random.randint(0,4)
    randomColumn = random.randint(0,4)
    
    #placing the computer ship
    array[randomRow][randomColumn] = "%"
    
    #getting the coordinates for the player ship (input verification through while loops
    guestRow = int(input("What row would you like to put your battleship on?:\n"))
    while (guestRow < 0 and guestRow > 4):
        guestRow = int(input("Your entered number was invalid, please enter a number between 0 and 4:\n"))
    guestColumn = int(input("What column would you like to put your battleship on?\n"))
    while (guestColumn < 0 and guestColumn > 4):
        guestColumn = int(input("Your entered number was invalid, please enter a number between 0 and 4:\n"))
    
    #placing the player ship
    array[guestRow][guestColumn] = "$"
    
    if (randomRow == guestRow and randomColumn == randomRow):
        print("Your battle ship ($) is sunk!")
    else:
        print("Your battle ship is still alive!")
        
    for subarray in array:
        print(subarray)
        
    print()
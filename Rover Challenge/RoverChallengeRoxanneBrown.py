from NewPosition import NewPosition
from Plateau import Plateau
from Rover import Rover

#Main program
#Introductory message 
print("Welcome to the Rover changing station, please make sure that all inputs are correct.")

#User inserts size of area (grid)
userAreainput = str(input("Set size of area: ")).split(" ")
plateau1 = Plateau(userAreainput[0], userAreainput[1])

#Added this so that one could enter as many rovers as they'd like 
amountRoversInput = int(input("How many Rovers would you like to change?: "))

#For loop to loop through the information on the  amount of rovers that would like to be enetered.
#Create an empty list for the amount of rovers entered
listRovers = []
for numRovers in range(amountRoversInput):
    newRover = Rover()
    #insert current position of rover, including the number of rover you are entering
    input1 = str(input(f'Insert current position of Rover {numRovers + 1}: ')).split(" ")
    newRover.SetCoord(input1[0], input1[1], input1[2])
    #Insert the change of coordinates that user would like to do on rover 
    newPosition1 = NewPosition()
    userMovementInput = str(input("Enter change of Coordinates: "))
    newPosition1.SetPosition(userMovementInput, newRover, plateau1)
    #add the new rovers entered to the list 
    listRovers.append(newRover)

#create a for loop to loop through the new rovers added to the list and print their indiviudual new cooridnates 
for rover in listRovers:
    print (rover.posx, " ", rover.posy, " " , rover.direction)

print()
plateau1.printGrid(listRovers) 

#create a rover class for each individual rover 
class Rover():
    posx = 0
    posy = 0
    direction = " "
    #create a method which sets coordinates and calls in the values which were entered 
    def SetCoord(self, x, y, newdir):
        Rover.posx = int(x)
        Rover.posy = int(y)
        Rover.direction = newdir 
        return Rover.posx, Rover.posy, Rover.direction

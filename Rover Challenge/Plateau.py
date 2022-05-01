from Cell import Cell

#create class of the area which was entered (i.e. the size of the grid)
class Plateau:
    width = 0 
    height = 0
    grid = []

    #constructor for the grid using the cell class imported from other file
    def __init__(self, w, h):
        self.width = int(w)
        self.height = int(h)

        for col in range(1, self.width + 1):
            for row in range(1, self.height + 1):
                newCell = Cell()
                newCell.X = row
                newCell.Y = col
                newCell.roverCount = 0
                self.grid.append(newCell)

    #doing below was difficult, I struggled to get decide which numbers to use to 
    #get the grid the right size and the rovers to show up on the grid in the correct place.
    def rangemethod(self, startnum, lastnum, step = 1):
        return range(startnum, lastnum + 1, step)

    def printGrid(self, rovers):
        for i in self.grid:
            i.roverCount = 0
            for rover in rovers:
                if rover.posx == i.X and rover.posy == i.Y:
                    i.roverCount += 1
   
        for row in reversed(self.rangemethod(1, self.height)):
            rowString = ""
            for col in range(1, self.width + 1):
                for j in self.grid:
                    if j.X == row and j.Y == col:
                        rowString += str(j.roverCount)
            print(rowString)
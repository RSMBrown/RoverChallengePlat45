class NewPosition():
    def SetPosition(self, setmovement, rover, plateau):
        listofMovements = list(setmovement)
        #change direction based off input and current direction 
        for mov in listofMovements:
            direction1 = rover.direction
            if direction1 == "N":
                if mov == "L":
                    rover.direction = "W"
                elif mov == "R":
                    rover.direction = "E"
            if direction1 == "E":
                if mov == "L":
                    rover.direction = "N"
                elif mov == "R":
                    rover.direction = "S"
            if direction1 == "S":
                if mov == "L":
                    rover.direction = "E"
                elif mov == "R":
                    rover.direction = "W"
            if direction1 == "W":
                if mov == "L":
                    rover.direction = "S"
                elif mov == "R":
                    rover.direction = "N"
            #change x or y based off enetered value as well as the direction
            if mov == "M" and rover.direction == "N":
                #make sure the rover doesnt fall off the outlined area
                if rover.posy + 1 <= plateau.width:
                    rover.posy += 1
            elif mov == "M" and rover.direction =="S":
                if rover.posy - 1 >= 0:
                    rover.posy -= 1

            if mov == "M" and rover.direction == "E":
                if rover.posx + 1 <= plateau.height:
                    rover.posx += 1
            elif mov == "M" and rover.direction =="W":
                if rover.posx - 1 >= 0:
                    rover.posx -= 1
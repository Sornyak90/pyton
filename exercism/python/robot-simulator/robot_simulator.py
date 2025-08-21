# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, instructions):
        cardinal_points = {0: NORTH, 1: EAST, 2: SOUTH, 3: WEST}
        orientation = {"R": 1, "L": -1}

        for instruction in instructions:
            if instruction == "A":
                if self.direction == NORTH:
                    x,y = self.coordinates
                    self.coordinates = (x, y+1)
                if self.direction == EAST:
                    x,y = self.coordinates
                    self.coordinates = (x+1, y)
                if self.direction == SOUTH:
                    x,y = self.coordinates
                    self.coordinates = (x, y-1)
                if self.direction == WEST:
                    x,y = self.coordinates
                    self.coordinates = (x-1, y)
            else:
                positions = cardinal_points[self.direction] + orientation[instruction]
                if positions > 3:
                    positions = 0
                if positions < 0:
                    positions = 3
                self.direction = cardinal_points[positions]
        




   

robot = Robot(NORTH, 7, 3)
robot.move("RAALAL")

print(robot.coordinates)
print(robot.direction)

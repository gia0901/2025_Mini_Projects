from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
EAT_TAIL_DISTANCE = 10
FOOD_DETECTION = 15

# Directions:
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def create_snake(self):
        # Default size of the snake is 3
        for idx in range(3):
            self.add_segment(STARTING_POS[idx])

    def move(self):
        # Move all the segments from the end:
        for idx in range(len(self.segments)-1, 0, -1):
            prev_x = self.segments[idx-1].xcor()
            prev_y = self.segments[idx-1].ycor()
            self.segments[idx].goto(prev_x, prev_y)
        self.head.forward(MOVE_DISTANCE)
    
    def extend(self):
        # Add a new segment which overriding on the last segment
        # In the 1st loop, snake is extend, except the new seg, the rest move forward
        # In the 2nd loop, the new seg is not override anymore, hence all the segments move normally
        self.add_segment(self.segments[len(self.segments)-1].position())
    
    def detect_food(self, food):
        return self.head.distance(food) < FOOD_DETECTION

    def detect_wall(self):
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280

    def detect_tail(self):
        # Loop through all segments.
        # If the head meets a segment in a very small distance (except [1] segment) 
        # -> The snake eats tail
        for seg in self.segments[2:]:
            if self.head.distance(seg) < EAT_TAIL_DISTANCE:
                return True


    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
    
    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
    
    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
    



from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.up()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment((self.segments[-1].xcor() - 20, self.segments[-1].ycor()))
        # print(self.segments[-1].xcor(), self.segments[-1].xcor() - 20)

    def move(self):
        segs = self.segments
        for seg_num in range(len(segs) - 1, 0, -1):
            new_x = segs[seg_num - 1].xcor()
            new_y = segs[seg_num - 1].ycor()
            segs[seg_num].goto(new_x, new_y)
        segs[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(20)
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.goto(-300, 300)
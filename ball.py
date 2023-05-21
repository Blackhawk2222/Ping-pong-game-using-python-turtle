from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def b(self):
        xc=self.xcor()
        yc=self.ycor()
        self.goto(xc+self.xmove,yc+self.ymove)

    def bouncey(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.move_speed*=0.9



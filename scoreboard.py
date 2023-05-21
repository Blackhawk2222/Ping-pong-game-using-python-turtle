from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 260)
        self.write(arg=self.lscore, align="center", font=("Arial", 20, "normal"))
        self.goto(-100, 260)
        self.write(arg=self.rscore, align="center", font=("Arial", 20, "normal"))


    def rinc(self):
        self.rscore+=1
        self.update()


    def linc(self):
        self.lscore+=1
        self.update()


    def gameover(self):
        k=""
        if self.lscore==5:
            k="Left side win"
        elif self.rscore==5:
            k="Right side win"
        elif self.lscore==5 and self.rscore==5:
            k="Game is a Draw"
        self.goto(0,0)
        self.write(arg=f"Game Over\n{k}",align="center",font=("Arial",20,"normal"))

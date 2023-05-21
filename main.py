from turtle import Turtle,Screen
from padd import Pad
from ball import Ball
from border import Border
from scoreboard import Score
import time
screen=Screen()
screen.title("Ping Pong")
screen.tracer(0)
#Drawing the border
bor=Border()
#Initialising the paddles
lpaddle=Pad(-270,0)
rpaddle=Pad(270,0)
screen.setup(height=600,width=600)
screen.bgcolor("black")
ball=Ball()
score=Score()
screen.listen()
screen.onkey(rpaddle.up,"Up")
screen.onkey(rpaddle.down,"Down")
screen.onkey(lpaddle.up,"w")
screen.onkey(lpaddle.down,"s")

game=True
while game is True:
    time.sleep(ball.move_speed)
    ball.b()
    #Make the ball bounce off of top and bottom sides
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    #Make the ball bounce off of paddles
    if ball.distance(rpaddle)<50 and ball.xcor()>250 or ball.distance(lpaddle)<50 and ball.xcor()<-250:
        ball.bouncex()
    #Make the ball reset and increase the respective score when ball goes out
    if ball.xcor()>280:
        score.update()
        score.rinc()
        ball.goto(0,0)
        ball.move_speed=0.1
        ball.bouncex()
    if ball.xcor()<-280:
        score.update()
        score.linc()
        ball.goto(0,0)
        ball.move_speed=0.1
        ball.bouncex()
    #Game over when one player reaches score 5
    if score.lscore==5 or score.rscore==5:
        score.gameover()
        ball.hideturtle()
        game=False
    screen.update()

screen.exitonclick()
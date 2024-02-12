from turtle import Screen,Turtle

import time

from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
game_is_on = True

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
score = Score()

ball = Ball()


# score = Score()

screen.listen()

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")



while game_is_on:
  time.sleep(ball.move_speed)
  ball.move()
  screen.update()

  # detect collision with upper and lower wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # detect collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :

    ball.bounce_x()

  # detect if ball goes out of r-bounds
  if ball.xcor() > 380:
    ball.reset_position()
    score.increase_l_score()
  
    
  # detect if ball goes out of l_bound
  elif ball.xcor() < -380:
    ball.reset_position()
    score.increase_r_score()
    
screen.exitonclick()


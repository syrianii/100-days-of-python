from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score


screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
game_is_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


while game_is_on:
  
  screen.update()
  time.sleep(0.15)

  snake.move() 
  if snake.head.distance(food) < 15:
    food.refresh()
    score.increase_score()
    snake.extend_snake()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    score.reset()
    snake.reset()

  for segment in snake.segments[1:]:
    
    if snake.head.distance(segment) < 10:
      score.reset()
      snake.reset()

    
  

screen.exitonclick()

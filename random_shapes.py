
from turtle import Turtle, Screen
import random

turtle = Turtle()


colors = ["black","green","blue","red","purple","grey","brown"]



def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    turtle.forward(100)
    turtle.right(angle)

for shape_side_n in range(3,11):
  turtle.color(random.choice(colors))
  draw_shape(shape_side_n)
 
    
      
    
    

screen = Screen()
screen.exitonclick()

import turtle as t 
import random 

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  custom_color = (r,g,b)
  return custom_color

def draw_spinegraph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

draw_spinegraph(1)
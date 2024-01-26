import turtle as tr
import random

t = tr.Turtle()

tr.colormode(255)
t.width(10)
t.speed("fastest")


directions = [0,90,180,270]

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  custom_color =  (r,g,b)
  return custom_color

for _ in range(200):
  t.pencolor(random_color())
  t.forward(30)
  
  t.setheading(random.choice(directions))
  
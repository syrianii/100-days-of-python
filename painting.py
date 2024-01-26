import turtle as t 
import colorgram
import random

# EXTRACT COLOR
# colors = colorgram.extract("colors.jpeg",10)
# new_colors = []
# for color in colors:
#   new_rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#   new_colors.append(new_rgb)
#   print(new_rgb)

color_list = [(58, 106, 148),
(224, 200, 109),
(134, 84, 58),
(223, 138, 62),
(196, 145, 171),
(141, 178, 204),
(139, 82, 105)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

number_of_dots = 100


for dot_count in range(1,number_of_dots):
  
  tim.dot(20,random.choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.setup(height = 500 , width = 500)

screen.exitonclick()

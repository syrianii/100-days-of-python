from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()



def move_forward(): 
  tim.forward(10)
  
def move_backward():
  tim.backward(10)

def move_anti_clockwise():
  new_heading = tim.heading() - 10
  tim.setheading(new_heading)

def move_clockwise():
  new_heading = tim.heading() + 10
  tim.setheading(new_heading)

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_anti_clockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear)
screen.listen()
screen.mainloop()
from turtle import Turtle

DISTANCE = 40
class Paddle(Turtle):
  def __init__(self,position):
    super().__init__()
    self.create_paddle(position)

  def create_paddle(self,position):
      self.shape("square")
      self.color("white")
      self.shapesize(stretch_len=1,stretch_wid=5)
      self.penup()
      self.goto(position)
      
  def up(self):
    new_y = self.ycor() + DISTANCE
    self.sety(new_y)

  def down(self):
    new_y = self.ycor() - DISTANCE
    self.sety(new_y)
      
    
  

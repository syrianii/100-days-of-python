from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",22,"bold")

class Score(Turtle):
  def __init__(self,):
    super().__init__()
    self.l_score = 0
    self.r_score = 0
    self.penup()
    self.color("white")
    self.write_score()
    self.hideturtle()
    

  def write_score(self):
    self.goto(-100,200)
    self.write(self.l_score, align=ALIGNMENT,
              font=FONT)
    self.goto(100,200)
    self.write(self.r_score, align=ALIGNMENT,
              font=FONT)

  def increase_l_score(self):
    self.l_score += 1
    self.clear()
    self.write_score()

  def increase_r_score(self):
    self.r_score += 1
    self.clear()
    self.write_score()

  
    
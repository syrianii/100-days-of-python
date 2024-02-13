from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNEMNT = "center"


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("black")
    self.goto(-200,250)
    self.level = 1
    self.write_score()
    self.hideturtle()
    

  def write_score(self):
    self.write(f"Level: {self.level}",align=ALIGNEMNT,font= FONT)

  def increase_level(self):
    self.level += 1
    self.clear()
    self.write_score()

  def game_over(self):
    self.setposition(0,0)
    self.write("Game Over", align = ALIGNEMNT, font = FONT)
  
    
    

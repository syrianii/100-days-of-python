from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",14,"normal")

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.highscore = 0
    self.read_highscore()
    
    self.penup()
    self.color("white")
    self.setposition(0,270)
    self.write_score()
    self.hideturtle()
    
    

  def write_score(self):
    
    self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT,
              font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.write_score()

  def reset(self):
    if self.score > self.highscore:
      self.high = self.score     
      self.write_highscore()

    self.score = 0

  def write_highscore(self):
    with open("highscore.txt", "w") as file:
      file.write(f"{self.highscore}")

  def read_highscore(self):
    with open("highscore.txt","r") as file:
      self.highscore = int(file.read())

  # def game_over(self):
  #   self.setposition(0,0)
  #   self.write("Game Over", align = ALIGNMENT, font = FONT)
  
    
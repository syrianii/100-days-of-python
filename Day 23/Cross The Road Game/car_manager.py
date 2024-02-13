from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
  def __init__(self):
    self.cars = []
    self.car_speed = STARTING_MOVE_DISTANCE
    
   

  def create_car(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      car = Turtle(shape="square")
      car.penup()
      car.color(random.choice(COLORS))
      car.shapesize(stretch_len = 2 ,stretch_wid=1)
      random_y = random.randint(-250,250)
      car.goto(300,random_y)
      self.cars.append(car)
    

  def move_cars(self):
    for car in self.cars:
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed += MOVE_INCREMENT
    


      
    

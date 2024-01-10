import math

def paint_calc(height,width,cover):
  numbers_of_can = (height * width) / cover
  numbers_of_can = math.ceil(numbers_of_can)
  print(f"You'll need {numbers_of_can} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

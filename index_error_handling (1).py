fruits = eval(input())

def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError :
    print("Fruit pie")
  else:
    print(fruit + "pie")
  finally:
    pass
    


  


make_pie(4)

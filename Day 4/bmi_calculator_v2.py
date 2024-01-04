### BMI Calculator2.0  (console)
user_weight = input("Please enter you weight (kg):\n")
user_height = input("Please enter you height (m):\n")
weight_as_int = int(user_weight)
height_as_float = float(user_height)
bmi = int(weight_as_int / (height_as_float**2))
if bmi < 18.5:
  print(f"Your BMI is {bmi},you are underweight.")
elif (bmi > 18.5) & (bmi < 25):
  print(f"Your BMI is {bmi},you are normal weight.")
elif (bmi > 25) & (bmi < 30):
  print(f"Your BMI is {bmi},you are overweight.")
elif (bmi > 30) & (bmi < 35):
  print(f"Your BMI is {bmi},you are obesse.")
elif bmi > 35:
  print(f"Your BMI is {bmi},you are clinically obesse.")

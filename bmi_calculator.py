### BMI Calculator  (console)
user_weight = input("Please enter you weight (kg):\n")
user_height = input("Please enter you height (m):\n")
weight_as_int = int(user_weight)
height_as_float = float(user_height)
bmi = int(weight_as_int / (height_as_float ** 2))
print("Body Mass Index is:\n",bmi)
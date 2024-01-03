print("Welcome to Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_names = name1 + name2
t_count = combined_names.count("t") 
r_count = combined_names.count("r") 
u_count = combined_names.count("u") 
e_count = combined_names.count("e") 
l_count = combined_names.count("l") 
o_count = combined_names.count("o") 
v_count = combined_names.count("v") 

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

score = (true_count * 10 ) + love_count 

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos")

elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}")

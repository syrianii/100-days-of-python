#to apply the hidden functionality of the max function

students_score = input("Enter a list of students score: ").split()
print(f"Students scores are : {students_score}")

highest_score = 0

for score in students_score:
  
  score = int(score)
  highest_score = int(highest_score)
  
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is : {highest_score}")
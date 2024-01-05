# to apply the hiddent functionality of sum and len functions
students_height = input("Enter students height: ").split()
total_height = 0
num_of_students = 0

for height in students_height:
  total_height += int(height)

for student in students_height:
  num_of_students += 1

average_student_height = round((total_height / num_of_students), 2)
print(f"Average student height is : {average_student_height}")
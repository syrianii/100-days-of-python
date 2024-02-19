import random
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
student_marks = {student:random.randint(1,100) for student in names}
print(student_marks)

passed_students ={student:mark for (student,mark) in student_marks.items() if int(mark) > 50}

print(passed_students)
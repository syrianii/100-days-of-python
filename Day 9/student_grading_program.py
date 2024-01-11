students = {
  "Harry":81,
  "Ron" :79,
  "hermione":99,
  "Darco":74,
  "Neville":62,
}

students_grad = {}

for key in students:
  grade = students[key]
  if grade > 90:
    students_grad[key] = 'Outstanding'
  elif grade > 80:
    students_grad[key] = 'Exceed Expectation'
  elif grade > 70:
    students_grad[key] = 'Acceptable'
  else:
    students_grad[key] = 'Fail'

print(students_grad)

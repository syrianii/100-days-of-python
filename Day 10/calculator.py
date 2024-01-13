def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


num1 = float(input("What's the first number?: "))

for operation in operations:
  print(operation)

symbol = input("Pick an operation from the line above : ")
calculation_function = operations[symbol]

num2 = float(input('Whats the second number?: '))

answer = calculation_function(num1, num2)
print(f"{num1} {symbol} {num2} = {answer}")

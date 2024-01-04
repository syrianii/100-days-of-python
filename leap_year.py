year = input("Please enter the year: ")
if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print("This is a year leap")
    else:
      print("This is not a leap year")
  else:
    print("This is a leap year")
else:
  print("This is not a leap year")

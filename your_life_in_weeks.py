# how many years, weeks, days are left in your life assuming that you will live till 90

age = input("how old are you?\n")
age_as_int = int(age)

years_left = 90 - age_as_int
weeks_left = years_left * 52
days_left = years_left * 364

print(f"You have {days_left} Days, {weeks_left} Weeks, {years_left} Years left.")
22
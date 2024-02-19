numbers = [1,2,3]
new_numbers = [number + 1 for number in numbers]

name = "Angela"
new_list = [letter for letter in name]

doubled_numbers = [number * 2 for number in range(1,5)]
print(doubled_numbers)

names = ['Alex','Beth','Carolina','Dave','Eleanor','Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

all_caps = [name.upper() for name in names if len(name) > 4]
print(all_caps)


# squared numbers

numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)


#filtering odd numbers

list_of_strings = input().split(",")

numbers = [int(item) for item in list_of_strings]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
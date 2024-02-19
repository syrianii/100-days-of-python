weather_c = eval(input())

weather_f = {day:((temp * 0.9)+32) for day,temp in weather_c.items()}
print(weather_c)
print(weather_f)
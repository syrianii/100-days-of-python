import pandas as pd 

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
values = data["Primary Fur Color"].value_counts()


Fur_color = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [values.iloc[0], values.iloc[1], values.iloc[2]]
}

fur_color_df = pd.DataFrame(Fur_color)

fur_color_df.to_csv("Squirrel_Color_Count.csv")




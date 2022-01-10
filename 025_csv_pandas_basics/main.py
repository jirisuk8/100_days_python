import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = df['Primary Fur Color'].value_counts()
print(df.groupby('Primary Fur Color').size())

# fur_colors.to_csv("squirrel_counts.csv")


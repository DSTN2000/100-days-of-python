import pandas as pd

squirrels = pd.read_csv('25/squirrels.csv')
print(len(squirrels[squirrels['Primary Fur Color'] == 'Black']))
colors = ['Black', 'Gray', 'Cinnamon']
color_dict = {'Fur color': [color for color in colors], 'Amount': [len(squirrels[squirrels['Primary Fur Color'] == color]) for color in colors]}
df = pd.DataFrame(color_dict)
df.to_csv('25/squirrels_df.csv')
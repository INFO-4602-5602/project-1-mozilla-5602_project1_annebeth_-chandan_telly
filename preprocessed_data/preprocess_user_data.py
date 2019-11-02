import pandas as pd

PATH_TO_DATA = # set a path to location of survey data here
df = pd.read_csv(PATH_TO_DATA, encoding='iso-8859-1')

# Rename the columns with very long names.
df.rename(columns={'Thinking about a future in which so much of your world is connected to the internet leaves you feeling:':'attitude',
                    'I consider myself:':'user_level'},
                 inplace=True)

# Also replace some of the very long value names.
df["user_level"] = df["user_level"].replace('Average User:.*', "Average User", regex=True)
df["user_level"] = df["user_level"].replace('Technically Savvy:.*', "Technically Savvy", regex=True)
df["user_level"] = df["user_level"].replace('Ultra Nerd:.*', "Ultra Nerd", regex=True)
df["user_level"] = df["user_level"].replace('Luddite:.*', "Luddite", regex=True)

df["attitude"] = df["attitude"].replace('A little wary.*', "A little wary", regex=True)
df["attitude"] = df["attitude"].replace('Cautiously optimistic.*', "Cautiously optimistic", regex=True)
df["attitude"] = df["attitude"].replace('On the fence.*', "On the fence", regex=True)
df["attitude"] = df["attitude"].replace('Super excited!.*', "Super excited!", regex=True)
df["attitude"] = df["attitude"].replace('Scared as hell.*', "Scared as hell", regex=True)

df_subset = pd.DataFrame()
df_subset['user_level'] = df['user_level']
df_subset['attitude'] = df['attitude']

# Group the data to get the total count per category
df_subset = df_subset.groupby(df_subset.columns.tolist()).size().reset_index().rename(columns={0:'counts'})

# Create a CSV for the user category data
df_subset.to_csv('user_categories.csv', index=False)

# Create a JSON for the user category data
df_subset.to_json('user_categories.json', orient="split", index=False)

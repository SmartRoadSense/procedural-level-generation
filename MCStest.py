import pandas as pd
import csv

data = pd.read_csv('mcs.csv', decimal='.', error_bad_lines=False, delimiter=',', quoting=csv.QUOTE_ALL)
#data['Coordinates'].values

#df = pd.DataFrame(data.row.str.split(',', 1).tolist(), columns = ['longitude','latitude'])

df = data['Coordinates'].str.split(',', expand=True).rename(columns = {1:'longitude',0:'latitude'})
df = df.assign(PerceivedTemperature = data['Perceived temperature'].values)

print(df.head())

df.to_csv('mcs-cleaned.csv', encoding='utf-8', index=False)

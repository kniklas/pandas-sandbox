"My docstring"

import pandas as pd

#  df = pd.read_csv('gapminder.tsv', sep='\t')
df = pd.read_excel('new_words.xlsx')
# print(df)
#  print(df.head())
#  print(df.tail())
#  print(df.shape)
#  print(df.columns)
#  print(df.dtypes)
#  print(df.info())
#  print(df['meaning 1'])
#  print(df['meaning 1'].iloc[2])

LAST_ROWS = 6
start_row = df.shape[0] - LAST_ROWS
end_row = df.shape[0]
meanings = ('meaning 1', 'meaning 2', 'meaning 3', 'meaning 4', 'meaning 5')

for i in range(start_row, end_row):
    print('\n' + df['word / phrase'].iloc[i],
          df['type'].iloc[i]+',', end='')
#  df['meaning 1'].iloc[i],
#  df['meaning 2'].iloc[i],
#  df['meaning 3'].iloc[i],
#  df['meaning 4'].iloc[i],
#  df['meaning 5'].iloc[i])
    #  print('LICZBA: ', df['def no'].iloc[i])
    if df['def no'].iloc[i] == 1:
        print(f"{df[meanings[0]].iloc[i]}", end=' ')
    else:
        for j in range(df['def no'].iloc[i]):
            print(f"{j+1}: {df[meanings[j]].iloc[i]}", end=' ')

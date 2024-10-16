"My docstring"

import pandas as pd

df = pd.read_excel('new_words.xlsx')
LAST_ROWS = 6
start_row = df.shape[0] - LAST_ROWS
end_row = df.shape[0]
meanings = ('meaning 1', 'meaning 2', 'meaning 3', 'meaning 4', 'meaning 5')

for i in range(start_row, end_row):
    # print word / phrase and type
    print('\n' + df['word / phrase'].iloc[i],
          df['type'].iloc[i]+',', end='')
    # handle simpler display if only one explanation
    if df['def no'].iloc[i] == 1:
        print(f"{df[meanings[0]].iloc[i]}", end=' ')
    # handle more complex display for multiple meanings
    else:
        for j in range(df['def no'].iloc[i]):
            print(f"{j+1}: {df[meanings[j]].iloc[i]}", end=' ')

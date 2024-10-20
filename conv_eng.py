"My docstring"

import warnings

import pandas as pd

FILE_NAME = 'new_words.xlsx'
FILE_PATH = '~/Desktop/English/'
LAST_ROWS = 4

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
df = pd.read_excel(FILE_PATH+FILE_NAME)
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

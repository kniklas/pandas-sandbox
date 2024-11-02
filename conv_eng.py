"Display last n rows of a file. "

import argparse as ap
import warnings

import pandas as pd

parser = ap.ArgumentParser(description='Display last n rows of a file')
parser.add_argument('-n', type=int, help='Number of rows to display')
parser.add_argument('file', type=str, help='File name')
args = parser.parse_args()

LAST_ROWS = args.n
FILE_NAME = args.file
SHEET_NAME = 'words list'

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
df = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME)
start_row = df.shape[0] - LAST_ROWS
end_row = df.shape[0]
meanings = ('meaning 1', 'meaning 2', 'meaning 3', 'meaning 4', 'meaning 5')

for i in range(start_row, end_row):
    # print word / phrase and type
    print(df['word / phrase'].iloc[i],
          df['type'].iloc[i]+',', end='')
    # handle simpler display if only one explanation
    if df['def no'].iloc[i] == 1:
        print(f"{df[meanings[0]].iloc[i]}", end='\n')
    # handle more complex display for multiple meanings
    else:
        for j in range(df['def no'].iloc[i]):
            print(f"{j+1}: {df[meanings[j]].iloc[i]}", end=' ')
        print()  # newline

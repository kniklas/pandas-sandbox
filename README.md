# Pandas Sandbox

Repository to experiment and learn pandas.


## Helper scripts to copy words into SuperMemo

Use `conv_eng.py` and `endisco.sh` to automate the process of copying and pasting words entered in Excel using a pre-defined format from the file: `words.xlsx`

It is recommended to copy `endisco.sh` file to a home or other path to execute the file easily from a shell and configure correctly the following environment variables:
* `CONV_ENG_DIR` - absolute directory path to `conv_eng.py` file
* `CONV_ENG_WORDS` - absolute directory path to Excel file with words, see: `words.xlsx` example

To change the number of last words available in the clipboard, execute 'endisco -n X where X specifies the number of words.

In [SuperMemo](https://supermemo.com), when editing the custom dictionary, import words and use the automatically generated clipboard.

Use `endisco_test.sh` to test locally how the solution works (no environment variables required).

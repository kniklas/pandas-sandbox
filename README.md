# Pandas Sandbox

Repository to experiment and learn pandas.


## Helper scripts to copy words into SuperMemo

Use `endisco.sh` to automate the process of copying and pasting words entered in Excel using a pre-defined format from the file: `words.xlsx`

It is recommended to copy `endisco.sh` file to a home or other path to execute the file easily from a shell and configure correctly the following environment variables:
* `CONV_ENG_DIR` - absolute directory path to `conv_eng.py` file
* `CONV_ENG_WORDS` - absolute directory path to Excel file with words, see: `words.xlsx` example

To change the number of last words taken from the Excel file, to be available in the clipboard, execute `./endisco.sh -n`, where `n` specifies the number of words. Execution of the script without a parameter uses the default set in the shell file.

In [SuperMemo](https://supermemo.com), when editing the custom dictionary, use import words feature and use the automatically generated clipboard.

Use `endisco_test.sh` to test the solution locally (no environment variables required).

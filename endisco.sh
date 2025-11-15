#!/bin/bash

# This script extracts a specified number of words from an Excel file and copies them to the clipboard. First parameter is the number of words to extract.

# Default values
DEFAULT_NO_OF_WORDS=3

# Environment variables
SCRIPT_DIR=$CONV_ENG_DIR
FILE_PATH=$CONV_ENG_WORDS_XLSX

NO_OF_WORDS=${1:-$DEFAULT_NO_OF_WORDS}

cd $SCRIPT_DIR && \
	python3 conv_eng.py \
	-n $NO_OF_WORDS $FILE_PATH | pbcopy

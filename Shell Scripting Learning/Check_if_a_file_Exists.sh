#!/bin/bash

FILE="/path/to/yourfile.txt"

if [ -f "$FILE" ]; then
echo "File" $FILE exists."
else
echo "File" $FILE does not exists."
fi 

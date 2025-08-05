#!/bin/bash

a=10
b=20

if [ $a -gt $b ]; then
    echo "a is greater than b"
else
    echo "b is greater than a"
fi

'''
# Prompt the user for input
read -p "Enter the value of a: " a
read -p "Enter the value of b: " b
'''

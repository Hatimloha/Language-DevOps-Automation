#!/bin/bash

for i in {1..5}; do
    touch "file$i.txt"
    echo "created file$i.txt"
done

#!/bin/bash

DIR="/path/to/yourdirectory"

if [ -d "$DIR" ]; then
  echo "Directory $DIR exists."
else
  echo "Directory $DIR does not exist. Creating it now..."
  mkdir -p "$DIR"
fi

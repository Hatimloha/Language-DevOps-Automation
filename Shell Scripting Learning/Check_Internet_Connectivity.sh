#!/bin/bash

if ping -c 1 gooogle.com &> /dev/null; then
  echo "Internet is connected"
else 
  echo "Internet connection is down."
fi

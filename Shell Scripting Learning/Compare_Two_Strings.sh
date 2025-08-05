#!/bin/bash

STRING1="Hello"
STRING2="World"

if ["$STRING1" = "$STRING2"]; then
  echo "The Strings are equal."
else
  echo "The strings are not equal "
fi

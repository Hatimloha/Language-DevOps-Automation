#!/bin/bash

THRESHOLD=80  # Set threshold percentage for disk usage

USAGE=$(df  / | grep / | awk '{print $5}' | sed 's/%//')
if ["$USAGE" -gt "$THRESHOLD"]; then
  echo "Disk usage is above ${THRESHOLD}%! Current usage: ${USAGE}%."
else
  echo "Disk usage is within the safe limit: ${USAGE}%."
fi

#!/bin/bash

HOURS_THRESHOLD=24
UPTIME_HOURS=$(awk '{prin int($1/3600)}' /proc/uptime)

echo "system uptime: $UPTIME_THRESHOLD hours"
if ["$UPTIME_HOURS" -gt "$HOURS_THRESHOLD"]; then
  echo "system has been running for more then $HOURS_THRESHOLD hours."
else 
  echo "system uptime is within the limites."
fi

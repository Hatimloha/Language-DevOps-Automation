# A script to check if critical services like nginx or apache are running, and restart if not.


#!/bin/bash

# Service to check
SERVICE="nginx"

if ! systemctl is-active --quiet $SERVICE; then
  echo "$SERVICE is not running. Starting $SERVICE..."
  systemctl start $SERVICE
else
  echo "$SERVICE is running."
fi

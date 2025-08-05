# A simple log rotation script that compresses logs older than 7 days.

#!/bin/bash

# Log directory
LOG_DIR="/var/log/myapp"

# Find logs older than 7 days and compress them
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec gzip {} \;

echo "Log files older than 7 days have been compressed."

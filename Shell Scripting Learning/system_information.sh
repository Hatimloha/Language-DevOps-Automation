# This script will help to print the system infomration like memory, disk, & CPU: 
#!/bin/bash

set -x # Enable debug mode to show each command before executi

df -h   # Displays disk space usage in human-readable format
free -g # Displays memory usage in gigabytes
nproc   # Shows the number of available processing units (CPU cores)
ps -ef  # Lists all running processes in the system

#!/bin/bash

# Script to check system resource usage

echo "CPU LOAD"
uptime

echo "Memory Usage"
free -m

echo "Disk Usage"
df -h

echo "Top 5 Processes by Memory Usage:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -6

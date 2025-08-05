#!/bin/bash

# This script checks for processes related to "amazon" and extracts the second field using awk.

# ps -ef:
# The 'ps -ef' command lists all currently running processes on the system in full format.
# This provides detailed information like process ID (PID), parent process ID (PPID), user running the process, and command details.

# grep "amazon":
# The output of 'ps -ef' is piped into 'grep', which filters the list of processes and shows only those containing the string "amazon".
# This is useful for searching for specific processes (in this case, processes with the keyword "amazon").

# awk -F "":
# Awk is used here with the field separator (-F ""), although no delimiter is set explicitly (empty string).
# '{print $2}' prints the second field from the output of 'grep', which typically corresponds to the second column in the 'ps' output.

ps -ef | grep "amazon" | awk -F "" '{print $2}'

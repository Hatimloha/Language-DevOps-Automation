# Crontab File and Syntax

The `crontab` is a command in Unix-like operating systems used to schedule tasks (cron jobs) to be executed at specified times or intervals.

## Crontab Syntax

Each line in the crontab file follows this basic format:

```bash
*  *  *  *  *  command-to-execute
│  │  │  │  │
│  │  │  │  │
│  │  │  │  └───── Day of the week (0 - 7) (Sunday is 0 or 7)
│  │  │  └───────── Month (1 - 12)
│  │  └──────────── Day of the month (1 - 31)
│  └─────────────── Hour (0 - 23)
└────────────────── Minute (0 - 59)
```

- `*`: Represents all possible values for that field (every minute, hour, day, etc.).
- Each field must be separated by a space.

## Example: Scheduling a Task to Run at 11:59 PM Every Day

We want to execute a script that retrieves system information at 11:59 PM every night and sends it to an email address.

### Step 1: Create the Script

First, create a shell script (e.g., `system_info.sh`) to collect system information.

```bash
#!/bin/bash

# Collect system information
df -h > /tmp/system_info.txt
free -g >> /tmp/system_info.txt
nproc >> /tmp/system_info.txt
ps -ef >> /tmp/system_info.txt

# Send the information to an email
mail -s "Daily System Info" your-email@example.com < /tmp/system_info.txt
```

Make the script executable:

```bash
chmod +x system_info.sh
```

### Step 2: Edit the Crontab

To run the script at 11:59 PM every night, use the following crontab entry:

```bash
59 23 * * * /path/to/system_info.sh
```

- `59`: The minute (59th minute).
- `23`: The hour (23:00 or 11:00 PM).
- `*`: Every day of the month.
- `*`: Every month.
- `*`: Every day of the week.

### Step 3: Add the Crontab Entry

To add this entry to your crontab, edit the crontab file by running:

```bash
crontab -e
```

Add the following line to schedule the script:

```bash
59 23 * * * /path/to/system_info.sh
```

This ensures that the script runs at 11:59 PM every night, gathering system information and emailing it to the specified email address.

## Options:
```bash
 -u <user>  define user
 -e         edit user's crontab
 -l         list user's crontab
 -r         delete user's crontab
 -i         prompt before deleting
 -n <host>  set host in cluster to run users' crontabs
 -c         get host in cluster to run users' crontabs
 -T <file>  test a crontab file syntax
 -s         selinux context
 -V         print version and exit
 -x <mask>  enable debugging
```

---

## Key Points

- Use `crontab -e` to edit the cron table.
- The time format is based on the 24-hour clock.
- Ensure the script you want to run is executable.
- Configure mail on your system to send emails from the command line. Ensure `mail` is installed and properly configured.

---

This cron setup is useful for automating system monitoring and getting daily reports via email.

# `logrotate` in Linux

`logrotate` is a system utility in Linux used to manage and automatically rotate log files. It helps prevent log files from consuming excessive disk space by compressing, deleting, or moving old log files and creating new ones for continued logging.

## Why Use `logrotate`?

- **Log rotation**: Automatically rotate logs when they become large or reach a certain age.
- **Compression**: Compress old logs to save space.
- **Retention**: Specify how many old logs to keep before they are deleted.
- **Custom schedules**: Rotate logs daily, weekly, monthly, or based on log file size.

---

## Basic `logrotate` Syntax

Log rotation behavior is defined in configuration files, typically located at `/etc/logrotate.conf` or in the `/etc/logrotate.d/` directory for individual service-specific configurations.

### Example Configuration Block:

```bash
/path/to/logfile {
    rotate 7
    daily
    compress
    delaycompress
    missingok
    notifempty
    create 0640 root adm
    postrotate
        systemctl reload myservice
    endscript
}
```

### Explanation:
- **`/path/to/logfile`**: The path to the log file that will be rotated.
- **`rotate 7`**: Keeps 7 rotated log files before deleting the oldest.
- **`daily`**: Rotates the log file daily (other options include `weekly`, `monthly`, and `size`).
- **`compress`**: Compresses the old log files to save space.
- **`delaycompress`**: Delays compression until the next rotation to allow processes to still write to the file.
- **`missingok`**: If the log file is missing, don't return an error.
- **`notifempty`**: If the log file is empty, do not rotate it.
- **`create 0640 root adm`**: After rotating, create a new log file with the specified permissions and ownership.
- **`postrotate`**: Executes a command after the log rotation. In this example, it reloads a service after rotation.

---

## Key Configuration Options

### 1. **Rotation Frequency**

You can specify how often the log files are rotated:

- `daily`: Rotate log files every day.
- `weekly`: Rotate log files once a week.
- `monthly`: Rotate log files once a month.
- `yearly`: Rotate log files once a year.
- `size <value>`: Rotate logs when they reach a specified size (e.g., `size 100M` for 100MB).

### 2. **Retention and Number of Rotations**

- `rotate <count>`: Specifies how many rotations (versions) of the log file to keep before deleting the oldest one.

### 3. **Compression**

- `compress`: Compresses the rotated log files (usually with gzip).
- `delaycompress`: Compresses logs after they’ve been rotated at least once. This is useful if your service may still need to write to the old file for a short period.
- `nocompress`: Disables compression.

### 4. **Empty Log Handling**

- `notifempty`: Don’t rotate log files if they are empty.
- `ifempty`: Rotates empty log files (default behavior if not specified).

### 5. **Handling Missing Log Files**

- `missingok`: Ignore errors if the log file is missing and continue without throwing an error.
- `nomissingok`: Throw an error if the log file is missing.

### 6. **Creating New Log Files**

- `create <mode> <owner> <group>`: After rotating, create a new log file with the specified permissions, owner, and group. For example, `create 0640 root adm`.

### 7. **Pre/Post Rotate Commands**

- `prerotate` and `postrotate`: These blocks allow you to execute commands before or after log rotation. For example, you might want to reload a service after the logs are rotated.

```bash
postrotate
    systemctl reload nginx
endscript
```

---

## Example `logrotate` Configuration for Apache Logs

Let’s say you have an Apache web server, and you want to rotate the logs in `/var/log/apache2/access.log` and `/var/log/apache2/error.log` daily, keep the last 7 logs, compress them, and reload Apache after the rotation.

### Configuration:

```bash
/var/log/apache2/*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 0640 root adm
    postrotate
        /usr/sbin/apachectl graceful > /dev/null 2>&1 || true
    endscript
}
```

- This configuration will rotate both `access.log` and `error.log` daily.
- It will compress old logs, keep the last 7 rotated logs, and reload Apache gracefully after rotating logs.

---

## Manual Log Rotation

If you want to manually force log rotation without waiting for the cron job, you can use:

```bash
logrotate -f /etc/logrotate.conf
```

This forces the log rotation according to the configuration file.

---

## Viewing Log Rotation Status

You can check `/var/lib/logrotate/status` to see the status of recent log rotations.

---

## Conclusion

`logrotate` is a powerful utility that helps manage logs efficiently by rotating, compressing, and maintaining logs, ensuring that log files do not grow uncontrollably. It provides flexible options for when and how logs are rotated, making it essential for system and application maintenance.

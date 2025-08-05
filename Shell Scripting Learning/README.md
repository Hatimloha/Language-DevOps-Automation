# Shell-Scripting
"This repository contains essential shell scripts for automating tasks, system administration, and DevOps workflows. It includes scripts for file management, process control, network monitoring, and more, with a focus on simplicity and efficiency."

# Shell Scripting Commands

This repository contains essential shell scripts for various system administration tasks, automation, and DevOps workflows. Below are some of the primary shell commands used in the scripts along with descriptions.

shebang `#!/bin/bash`

## Main Shell Commands

### 1. `echo`
The `echo` command is used to display a message or text on the terminal. Commonly used for printing status messages or outputs in scripts.

```bash
echo "Hello, World!"
```

### 2. `ls`
The `ls` command lists the files and directories in the current working directory. Useful for checking contents and verifying file locations.

```bash
ls -l
```

### 3. `cd`
The `cd` (change directory) command is used to navigate between directories in the shell.

```bash
cd /path/to/directory
```

### 4. `pwd`
Displays the current working directory.

```bash
pwd
```

### 5. `cp`
The `cp` command is used to copy files or directories from one location to another.

```bash
cp source.txt destination.txt
```

### 6. `mv`
The `mv` command moves or renames files and directories.

```bash
mv oldname.txt newname.txt
```

### 7. `rm`
Used to remove files or directories.

```bash
rm filename.txt
```

### 8. `touch`
Creates an empty file or updates the timestamp of an existing file.

```bash
touch newfile.txt
```

### 9. `chmod`
Changes the permissions of a file or directory.

```bash
chmod 755 script.sh
```

### 10. `grep`
Searches for specific patterns within files.

```bash
grep "search-term" file.txt
```

### 11. `find`
Searches for files in a directory hierarchy.

```bash
find /path/to/search -name filename.txt
```

### 12. `ps`
Displays a list of running processes.

```bash
ps aux
```

### 13. `top`
Displays real-time information about running processes, including CPU and memory usage.

```bash
top
```

### 14. `df`
Shows disk space usage of file systems.

```bash
df -h
```

### 15. `du`
Displays disk usage of files and directories.

```bash
du -sh /path/to/directory
```

### 16. `tar`
Used to compress or extract tarball (.tar) archives.

```bash
tar -czvf archive.tar.gz /path/to/folder
```

### 17. `curl`
Transfers data from or to a server, often used for interacting with APIs.

```bash
curl https://api.example.com
```

### 18. `wget`
Downloads files from the web.

```bash
wget https://example.com/file.zip
```

### 19. `awk`
A powerful text processing tool used for pattern scanning and processing.

```bash
awk '{ print $1 }' file.txt
```

### 20. `sed`
Stream editor used for modifying and transforming text in files.

```bash
sed 's/old/new/g' file.txt
```

## Text File Editors

### 1. `nano`
A simple command-line text editor, easy to use for quick file editing.

```bash
nano script.sh
```

### 2. `vim`
A more advanced text editor with powerful features for editing code. Requires knowledge of Vim commands.

```bash
vim script.sh
```

### 3. `gedit`
A graphical text editor for GNOME environments, useful for editing scripts in a user-friendly interface.

```bash
gedit script.sh
```

---

Feel free to contribute by adding more commands or improving existing scripts!

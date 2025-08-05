# Using Pipe (`|`) in Shell Scripting

In shell scripting, the pipe (`|`) is used to send the output of one command as input to another command. It allows you to combine multiple commands to perform complex tasks efficiently.

## Syntax

```bash
command1 | command2
```

The output of `command1` is sent as the input to `command2`.

## Example: Using `grep` with Pipe

The `grep` command is used to search for specific patterns in text or files. When used with a pipe, it can filter the output of other commands.

### Example 1: Filtering `ls` Output

If you want to list all `.txt` files in the current directory, you can combine `ls` and `grep` using a pipe.

```bash
ls | grep ".txt"
```

- `ls`: Lists all files in the current directory.
- `grep ".txt"`: Filters the output to only show files with the `.txt` extension.

### Example 2: Checking Running Processes with `ps` and `grep`

To check if a specific process (e.g., `nginx`) is running, you can combine the `ps` command with `grep`.

```bash
ps aux | grep "nginx"
```

- `ps aux`: Lists all running processes.
- `grep "nginx"`: Filters the output to show only the processes that include `nginx` in their name.

### Example 3: Searching in Log Files with `cat` and `grep`

You can search for a specific error in a log file using the `cat` command with a pipe to `grep`.

```bash
cat /var/log/syslog | grep "error"
```

- `cat /var/log/syslog`: Displays the contents of the syslog file.
- `grep "error"`: Filters the log file content to show only lines containing the word "error".

---

## Combining Multiple Pipes

You can chain multiple pipes together to perform more complex tasks. For example, you can use `ps`, `grep`, and `wc` to count the number of times a process appears.

```bash
ps aux | grep "nginx" | wc -l
```

- `ps aux`: Lists all running processes.
- `grep "nginx"`: Filters for `nginx` processes.
- `wc -l`: Counts the number of lines (i.e., number of `nginx` processes).

---

## Key Points

- The pipe (`|`) sends the output of one command to another.
- It allows chaining of commands for more powerful operations.
- Common use cases include filtering with `grep`, counting lines with `wc`, and sorting output with `sort`.

---

Feel free to explore more by combining different commands using pipes to perform powerful shell scripting tasks!

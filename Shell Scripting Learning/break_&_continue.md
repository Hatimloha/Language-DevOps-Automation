# `break` and `continue` in Shell Scripting

In shell scripting, the `break` and `continue` statements are used to control the flow of loops such as `for`, `while`, and `until` loops.

## 1. **`break` Statement**

The `break` statement is used to exit the current loop prematurely. When `break` is encountered, the loop is immediately terminated, and the script continues with the next line of code after the loop.

### Syntax:

```bash
break
```

### Example: Using `break` in a `for` loop

```bash
#!/bin/bash

# Loop through numbers 1 to 10
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        # Exit the loop if the value of i equals 5
        break
    fi
    echo "Number: $i"
done

echo "Loop terminated."
```

### Output:

```bash
Number: 1
Number: 2
Number: 3
Number: 4
Loop terminated.
```

In this example, the loop terminates when `i` equals 5, skipping the rest of the loop iterations.

---

## 2. **`continue` Statement**

The `continue` statement is used to skip the current iteration of the loop and move to the next iteration. It does not exit the loop but rather jumps to the next cycle, skipping the rest of the commands in the current iteration.

### Syntax:

```bash
continue
```

### Example: Using `continue` in a `for` loop

```bash
#!/bin/bash

# Loop through numbers 1 to 10
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        # Skip the iteration where i equals 5
        continue
    fi
    echo "Number: $i"
done

echo "Loop completed."
```

### Output:

```bash
Number: 1
Number: 2
Number: 3
Number: 4
Number: 6
Number: 7
Number: 8
Number: 9
Number: 10
Loop completed.
```

In this example, when `i` equals 5, the `continue` statement causes the loop to skip that iteration, so 5 is not printed.

---

## Key Differences Between `break` and `continue`

| Command  | Behavior |
|----------|----------|
| `break`  | Terminates the entire loop immediately and moves on to the code following the loop. |
| `continue` | Skips the current iteration and jumps to the next iteration of the loop. |

---

## Example: Using `break` and `continue` Together

```bash
#!/bin/bash

# Loop through numbers 1 to 10
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        # Skip the iteration where i equals 5
        continue
    fi

    if [ $i -eq 8 ]; then
        # Exit the loop if the value of i equals 8
        break
    fi

    echo "Number: $i"
done

echo "Loop control with break and continue."
```

### Output:

```bash
Number: 1
Number: 2
Number: 3
Number: 4
Number: 6
Number: 7
Loop control with break and continue.
```

In this example:
- The `continue` statement skips the iteration where `i` equals 5.
- The `break` statement terminates the loop when `i` equals 8.

---

## Conclusion

- **`break`** is used to terminate the loop early.
- **`continue`** is used to skip an iteration and move to the next one.
- Both are useful for controlling loop execution in a more granular way.

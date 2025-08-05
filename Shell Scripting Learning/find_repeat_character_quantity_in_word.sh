# find the number of time "s" is coming in the word

#!/bin/bash
x = mississipi

grep - o "s" <<<"$x" | wc -l

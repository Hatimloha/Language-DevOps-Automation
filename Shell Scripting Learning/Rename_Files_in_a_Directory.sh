# A script to download multiple files from a list of URLs saved in a text file.

#!/bin/bash

# File containing list of URLs
URL_FILE="urls.txt"

# Download each URL in the list
while IFS= read -r URL; do
    wget "$URL"
done < "$URL_FILE"

echo "All files have been downloaded."

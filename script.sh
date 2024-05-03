#!/bin/bash

# Create the bin folder if it doesn't exist
mkdir -p bin

# Find all executable files in the current directory
find . -type f -executable -exec mv {} bin/ \;
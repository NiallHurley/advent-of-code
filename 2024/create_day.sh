#!/bin/bash

DAY=$1
FOLDER="2024"
DAY_FOLDER="${FOLDER}/day_$(printf "%02d" $DAY)"

# Create day folder
mkdir -p "$DAY_FOLDER"

# Copy the template file
cp "${FOLDER}/day_template.py" "${DAY_FOLDER}/day_$(printf "%02d" $DAY).py"

# Create input files
touch "${DAY_FOLDER}/day_$(printf "%02d" $DAY)_input.txt"
touch "${DAY_FOLDER}/day_$(printf "%02d" $DAY)_test_input.txt"

echo "Files created for Day $DAY in $DAY_FOLDER"
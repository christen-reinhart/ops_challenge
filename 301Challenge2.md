#!/bin/bash

# Define constants
SOURCE_FILE="/var/log/syslog"
DESTINATION_DIR="$(pwd)"  # Current working directory

# Get the current date and time in the format YYYY-MM-DD_HH-MM-SS
CURRENT_DATE_TIME=$(date +"%Y-%m-%d_%H-%M-%S")

# Construct the destination filename with the current date and time
DESTINATION_FILE="${DESTINATION_DIR}/syslog_${CURRENT_DATE_TIME}.log"

# Copy the syslog file to the current working directory
cp "${SOURCE_FILE}" "${DESTINATION_FILE}"

# Display a message indicating the completion of the operation
echo "Syslog file copied to: ${destination_file}"
#!/bin/bash

# Define the backup directory
backup_dir="/var/log/backups"

# Ensure the backup directory exists
mkdir -p "$backup_dir"

# Get the current timestamp
timestamp=$(date "+%Y%m%d%H%M%S")

# Log files to be cleared and compressed
log_files=("/var/log/syslog" "/var/log/wtmp")

# Function to clear and compress log files
clear_and_compress_logs() {
  for log_file in "${log_files[@]}"; do
    # Print the original file size
    original_size=$(du -h "$log_file" | cut -f1)
    echo "Original size of $log_file: $original_size"

    # Compress the log file to the backup directory
    compressed_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
    gzip -c "$log_file" > "$compressed_file"

    # Clear the contents of the log file
    echo -n > "$log_file"

    # Print the size of the compressed file
    compressed_size=$(du -h "$compressed_file" | cut -f1)
    echo "Compressed size of $compressed_file: $compressed_size"

    # Compare sizes
    echo "Size comparison:"
    echo "Original size: $original_size"
    echo "Compressed size: $compressed_size"
    echo
  done
}

# Call the function
clear_and_compress_logs
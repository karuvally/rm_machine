#!/usr/bin/env python3
# Script to remove files older than three months

# TODO
# Disk usage percent should be argument
# Removal should happen only if --remove-files is passed

# Import serious stuff
import os
import shutil
import argparse
from datetime import datetime
import pdb


# Generate list of files to be deleted
def generate_list(start_path):
    # List of files to be removed
    remove_list = []

    # Generate a datetime object
    current_time = datetime.now()

    # Find files older than three months under start_path
    for root, directories, files in os.walk(start_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            modified_time = datetime.fromtimestamp(
                os.path.getmtime(file_path)
            )
            file_age = current_time - modified_time
            if file_age.days > 90:
                remove_list.append(file_path)
    return remove_list

# The main function
def main(parser):
    # Parse the arguments
    arguments = parser.parse_args()

    # Calculate disk usage
    disk_usage = shutil.disk_usage(arguments.path)
    disk_usage_percent = (disk_usage.used / disk_usage.total) * 100

    # Do a cleanup if disk usage greater than 80%
    if disk_usage_percent > 80:
        files_to_remove = generate_list(arguments.path)
    for file_path in files_to_remove:
        os.remove(file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Remove files older than 3 months if disk usage > 80%"
    )
    parser.add_argument(
        "--path",
        type = str,
        required = True,
        help = "Path where cleanup is to be done"
    )
    parser.add_argument(
        "--remove-files",
        default = False,
        action = "store_true"
        help = "Enable removal of files"
    )

    # Call the main function
    main(parser)
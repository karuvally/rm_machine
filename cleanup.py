#!/usr/bin/env python3
# Script to remove files older than three months

# Import serious stuff
import os
import shutil
import argparse
from datetime import datetime
import pdb


# Generate list of files to be deleted
def generate_list(start_path, oldfile_age):
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
            if file_age.days > oldfile_age:
                remove_list.append(file_path)
    return remove_list


# The main function
def main(parser):
    # Parse the arguments
    arguments = parser.parse_args()

    # Calculate disk usage
    disk_usage = shutil.disk_usage(arguments.path)
    disk_usage_percent = (disk_usage.used / disk_usage.total) * 100

    # Find files older than three months
    files_to_remove = generate_list(arguments.path, arguments.oldfile_age)

    # Delete older files if disk usage > arguments.disk_usage %
    if disk_usage_percent > arguments.disk_usage and arguments.remove_files:
        for file_path in files_to_remove:
            print("[Info]: Removing", file_path)
            os.remove(file_path)
    elif disk_usage_percent < arguments.disk_usage and arguments.remove_files:
        print("Disk usage below", str(arguments.disk_usage) + "%")
    elif files_to_remove:
        print("No files will be deleted...")
        print("Printing files older than", arguments.oldfile_age, "day(s)")
        for file_path in files_to_remove:
            print(file_path)


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
        action = "store_true",
        help = "Enable removal of files"
    )
    parser.add_argument(
        "--oldfile-age",
        type = int,
        default = 90,
        help = "Files older than oldfile-age will be deleted, default: 90 days"
    )
    parser.add_argument(
        "--disk-usage",
        type = int,
        default = 80,
        help = "Removal files only if disk-usage > given percent (default: 80)"
    )
    # Call the main function
    main(parser)

#!/usr/bin/env python3
# Script to remove files older than three months

# Import serious stuff
import os
import shutil
from datetime import datetime
import pdb


# Generate list of files to be deleted
def generate_list(start_path):
    # List of files to be removed
    remove_list = []

    # Generate a datetime object
    current_time = datetime.now()

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
def main():
    pass            


generate_list("/home/sreedevi")

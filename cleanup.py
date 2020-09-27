#!/usr/bin/env python3
# Script to remove files older than three months

# Import serious stuff
import os
import datetime


# Generate list of files to be deleted
def generate_list(start_path):
    # Generate a datetime object
    date_obj = datetime.datetime.now()

    for root, directories, files in os.walk(start_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            
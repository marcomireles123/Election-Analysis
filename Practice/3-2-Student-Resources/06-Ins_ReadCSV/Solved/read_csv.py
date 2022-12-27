# First we'll import the os module
# This will allow us to create file paths across operating systems
    # Creates dynamic paths to external files that function across different OS's
import os

# Module for reading CSV files
    # This utilizes csv reader to translate the object being opened
    # Take note of the delimiter=' ' parameter
        # This tells python that each comma within the CSV should be seen as moving into a new column for a row
import csv

csvpath = os.path.join('..', 'Resources', 'accounting.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

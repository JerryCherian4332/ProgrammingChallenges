#!/usr/bin/env python3

import sys
import os


class CSV_Combiner:
    def __init__(self, files):
        # Checks that files are all .csv files
        for arg in files:
            if not arg.endswith(".csv"):
                print("One of the files does not end with .csv. Try again.")
                sys.exit(1)
        self.files = files

    def combine(self, files):
        # Goes through each file
        for fileNum, filename in enumerate(files):
            basename = os.path.basename(filename)
            try:
                # Checks for header row
                first_row = True
                # Tries to open file. Exits otherwise.
                with open(filename) as f:
                    # Combine each line
                    for line in f:
                        line = line.strip("\n")
                        # If it is not the first file and the line is the header row. Don't want to output header so
                        # continue.
                        if first_row and fileNum > 0:
                            first_row = False
                            continue
                        # If it is an empty line, continue
                        elif line == "":
                            continue
                        # If it is the first file and the line is the header row, output and add column name
                        elif first_row:
                            print(line + "," + "\"filename\"")
                            first_row = False
                        # Otherwise combine line with file name
                        else:
                            print(line + "," + "\"" + basename + "\"")
            # Handles error when file cannot be opened.
            except FileNotFoundError:
                print(filename + " cannot be found/opened. All the files up to the file have been combined. Try again.")
                return 1
        return 0


if __name__ == "__main__":
    # Takes in files
    args = list(sys.argv)[1:]
    # Error checking for arguments
    if len(args) < 1:
        print("Try again. Missing csv files to combine. Usage: csv_combiner.py [files].")
        quit()
    # Initializes CSV_combiner class
    combiner = CSV_Combiner(args)
    # Calls combine method
    combiner.combine(args)

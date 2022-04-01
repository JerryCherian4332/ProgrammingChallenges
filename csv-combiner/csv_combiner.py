#!/usr/bin/env python3

import sys
import os

class CSV_Combiner:
    def __init__(self, files):
        for arg in files:
            if not arg.endswith(".csv"):
                print("One of the files does not end with .csv. Try again.")
                sys.exit(1)
        self.files = files

    def combine(self, files):
        for fileNum, filename in enumerate(files):
            basename = os.path.basename(filename)
            try:
                first_row = True
                with open(filename) as f:
                    for line in f:
                        line = line.strip("\n")
                        if first_row and fileNum > 0:
                            first_row = False
                            continue
                        elif line == "":
                            continue
                        elif first_row:
                            print(line + "," + "\"filename\"")
                            first_row = False
                        else:
                            print(line + "," + "\"" + basename + "\"")
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
    combiner = CSV_Combiner(args)
    combiner.combine(args)
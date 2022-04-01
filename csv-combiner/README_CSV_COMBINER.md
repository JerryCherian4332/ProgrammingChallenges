# CSV - Combiner

## By Jerry Cherian

The csv_combiner.py file contains the main code for the combiner. This file contains the CSV_Combiner class. The combine method can 
be used to combine csv files with the respective filename at the end. The csv files must all have the same columns.

The code will output the combined files to stdout.

The file was ran and tested in a linux environment. It is intended to be run like this: 

python3 csv_combiner.py [files]

- [files] should be csv files separated by a space.

ex. python3 csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv

The csv_combiner_tester.py file does basic unit tests to ensure the combining works properly.

A sample run file is attached as combined.csv.
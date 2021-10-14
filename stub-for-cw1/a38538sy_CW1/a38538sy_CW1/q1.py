"""
Q1 is a script that returns, for each student, their ID and the total number of points they have scored. 
 
You should create and write your results into a .csv file
with 2 columns, one named "Username" (*exactly* what's between the quotes)
and "RawMark" (*exactly* what's between the quotes).

The stub contains three function stubs, `read_data_file`, `calculate_grades`, and
`write_report`. You should modify the bodies of these functions so they behave
appropriately.

You can replace the whole body of these functions if you wish, but they must be call-able
with the given arguments.
"""

# You may not import *any other modules*. This is the final and only import structure!
# You will want to use the Decimal class in case some marks are fractional (e.g., 4.5 out of 5)

import csv
from decimal import Decimal

def smart_round(x,n): #function rounds float to 2 decimal points and return str type
    return str(Decimal(x).quantize(Decimal('0.00')))

def read_data_file(filename):
    _dict = {}
    with open(filename) as csvfile:
        # There are two parsing classes in Python's standard csv module,
        # the object returned by `reader` and DictReader.
        # Pick the one you prefer!
        # https://docs.python.org/3.8/library/csv.html#reader-objects
        reader =  csv.DictReader(csvfile)
        for row in reader:
            score = 0
            if(row['Auto Score']) == '':
                score = float(row['Manual Score'])
            else:
                score= float(row['Auto Score']) 
            if(row['Username'] in _dict):
                _dict[row['Username']] = score + _dict[row['Username']]
            else:
                _dict[row['Username']] = score
        # You'll want to pull in the data into a data structure of your choice
        # e.g., a list of lists, a list of dictionaries...whatever you find convenient.
        # The different readers return different representations of rows.
    return _dict
        
def calculate_raw_grades(data):
        # You need to define your own data structure for collecting
        # grades for each student. We put in a dummy list just to make
        # the stub run. You should carefully consider what structure is
        # appropriate.
        grades = data
        return grades

def write_report(grades, filename):        
    with open(filename, 'w') as outfile:
        # Again, we just put "writer" as a default. You may prefer a DictWriter
        headerNames = ['Username','RawMark']
        writer = csv.DictWriter(outfile,fieldnames = headerNames)
        writer.writeheader()
        for each in grades.items():
            writer.writerow({headerNames[0]:each[0], headerNames[1]: smart_round(each[1],2)})

# Do not alter the code below here!
# This is used by the test harness!
# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.

if __name__ == '__main__':
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Calculate some raw grades!')
    parser.add_argument('source', type=str, default='exam_for_2020.csv', nargs='?',
                    help='the name of the csv file with grade data to be processed')
    parser.add_argument('target', type=str, default='q1Out.csv', nargs='?',
                    help='the name of the csv file where processed data gets written')

    args = parser.parse_args()
    data = read_data_file(args.source)
    write_report(calculate_raw_grades(data), args.target)

"""
Q2 is a script that returns, for each student, their ID and
the percentage (of all available points) they have scored. 
   
You should create and write your results into a .csv file q2Out.csv
 with 2 columns and the header row Username and PercentageMark.

You may not import *any other modules*. This is the final and only import structure!
You will want to use the Decimal class to avoid potential rounding issues.
"""

import csv
from decimal import Decimal
from os import write

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


def calculate_percentage_grades(data):
        # You need to define your own data structure for collecting
        # grades for each student. We put in a dummy list just to make
        # the stub run. You should carefully consider what structure is
        # appropriate.

        grades = data
                
        # You need to gather *more* data from the source than in q1!
        # Don't forget to round the percentage grade to 2 decimal places,
        # e.g., 69.23
 
        # You are allowed to create additional functions if it helps
        # you manage your code.
 
        return grades

def write_report(grades, filename):        
    with open(filename, 'w') as outfile:
        headerNames = ['Username','PercentageMark']
        # Again, we just put "writer" as a default. You may prefer otherwise
        # Don't forget to put in the header row!
        writer = csv.DictWriter(outfile,fieldnames=headerNames)
        writer.writeheader()
        for each in grades.items():
            writer.writerow({headerNames[0]:each[0], headerNames[1]: smart_round(each[1]*10,2)+ '%'})

        
# Do not alter the code below here!
# This is used by the test harness!
# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.
# It's almost the same as in q1.py. Slight change to the default for target and
# updates to the help text.
if __name__ == '__main__':
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Calculate some percentage marks!')
    parser.add_argument('source', type=str, default='exam_for_2020.csv', nargs='?',
                    help='the name of the csv file with grade data to be processed')
    parser.add_argument('target', type=str, default='q2Out.csv', nargs='?',
                    help='the name of the csv file where processed data gets written')

    args = parser.parse_args()

    data = read_data_file(args.source)
    write_report(calculate_percentage_grades(data), args.target)

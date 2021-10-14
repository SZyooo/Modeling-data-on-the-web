"""
Q5 is a script that returns the average (across all students) raw mark for the exam. 
   
You should create and write your results into a .csv file q5Out.csv
with 1 column and the header row AverageMark

You may not import *any other modules*. This is the final and only import structure!
You will want to use the Decimal class to avoid potential rounding issues.
"""

import csv
from decimal import Decimal

def smart_round(x,n): #function rounds float to 2 decimal points and return str type
    return str(Decimal(x).quantize(Decimal('0.00')))

def read_data_file(filename):
    with open(filename) as csvfile:
        _dict = {}
        # There are two parsing classes in Python's standard csv module,
        # the object returned by `reader` and DictReader.
        # Pick the one you prefer!
        # https://docs.python.org/3.8/library/csv.html#reader-objects
        reader =  csv.DictReader(csvfile)
        for row in reader:
            if(row['Username'] not in _dict):
                _dict[row['Username']] = 0
            score = 0
            if(row['Auto Score'] == ''):
                score = float(row['Manual Score'])
            else:
                score = float(row['Auto Score'])
            _dict[row['Username']] += score
        # You'll want to pull in the data into a data structure of your choice
        # e.g., a list of lists, a list of dictionaries...whatever you find convenient.
        # The different readers return different representations of rows.
        return _dict
        
def calculate_average(data):
        # You need to define your own data structure for collecting
        # grades for each student. We put in a dummy list just to make
        # the stub run. You should carefully consider what structure is
        # appropriate.
        ave_grade = 0
        total_score = 0
        num = 0
        for item in data.items():
            num += 1
            total_score += item[1]
        ave_grade = 1.0 * total_score / num
                
        # You need to gather *more* data from the source than in q1 or q2
 
        # You are allowed to create additional functions if it helps
        # you manage your code.

        return ave_grade

def write_report(grade, filename):        
    with open(filename, 'w') as outfile:
        # Again, we just put "writer" as a default. You may prefer otherwise
        # Don't forget to put in the header row!
        header = ['AverageMark']
        writer = csv.DictWriter(outfile,header)
        writer.writeheader()
        writer.writerow({header[0]:smart_round(grade,2)})

# Do not alter the code below here!
# This is used by the test harness!
# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.
# It's almost the same as in q1.py. Slight change to the default for target and
# updates to the help text.
if __name__ == '__main__':
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Calculate the class average!')
    parser.add_argument('source', type=str, default='exam_for_2020.csv', nargs='?',
                    help='the name of the csv file with grade data to be processed')
    parser.add_argument('target', type=str, default='q5Out.csv', nargs='?',
                    help='the name of the csv file where processed data gets written')

    args = parser.parse_args()

    data = read_data_file(args.source)
    write_report(calculate_average(data), args.target)

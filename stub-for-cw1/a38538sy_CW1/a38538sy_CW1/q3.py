"""
Q3 is a script that returns, for each student, their ID, the number of points 
scored on the autograded questions, the number of points scored on the manually graded 
  questions, and total number of points scored. 
   
You should create and write your results into a .csv file q3Out.csv
with 4 columns and the header row Username, RawAutogradedMark, RawManualMark, RawTotalMark.

You may not import *any other modules*. This is the final and only import structure!
You will want to use the Decimal class to avoid potential rounding issues.
"""

import csv
from decimal import Decimal

# Before this point, you will have noticed that the basic format of the 
# scripts are the same. Open the source and read into a structure. Process the data.
# Open the target and write out. Your read and write functions might look the same!
# As we've structured it, we load *all* of the data then massage *all* of the data
# in memory! So we have about twice the initial data in memory at the peak.
# It's worth asking whether this is necessary or whether we can process things in a more
# stream oriented way. What's the *problem based* max memory needed?

# Similarly, you might consider how you'd make a single script with all these functions
# so they'd form a single, coherent, library.

def smart_round(x,n): #function rounds float to 2 decimal points and return str type
    return str(Decimal(x).quantize(Decimal('0.00')))

def read_data_file(filename):
    with open(filename) as csvfile:
        # There are two parsing classes in Python's standard csv module,
        # the object returned by `reader` and DictReader.
        # Pick the one you prefer!
        # https://docs.python.org/3.8/library/csv.html#reader-objects
        _dict = {}
        reader =  csv.DictReader(csvfile)
        for row in reader:
            scores = [0,0,0]# auto, manual, total
            auto_score,manual_score = 0,0
            if(row['Auto Score']!=''):
                auto_score = float(row['Auto Score'])
            if(row['Manual Score']!=''):
                manual_score = float(row['Manual Score'])
            if(row['Username'] in _dict):
                _dict[row['Username']][0] = _dict[row['Username']][0] + auto_score
                _dict[row['Username']][1] = _dict[row['Username']][1] + manual_score
            else:
                _dict[row['Username']] = [0.0,0.0,0.0]
                _dict[row['Username']][0] = auto_score             
                _dict[row['Username']][1] = manual_score
        for each in _dict.items():
            each[1][2] = each[1][0] + each[1][1]

        # You'll want to pull in the data into a data structure of your choice
        # e.g., a list of lists, a list of dictionaries...whatever you find convenient.
        # The different readers return different representations of rows.

        return _dict

def calculate_marks_breakdown(data):
        # You need to define your own data structure for collecting
        # grades for each student. We put in a dummy list just to make
        # the stub run. You should carefully consider what structure is
        # appropriate.

        grades = data
                
        # You need to gather *more* data from the source than in q1 or q2
 
        # You are allowed to create additional functions if it helps
        # you manage your code.
 
        return grades
    
def write_report(grades, filename):        
    with open(filename, 'w') as outfile:
        # Again, we just put "writer" as a default. You may prefer otherwise
        # Don't forget to put in the header row!
        headers = ['Username','RawAutogradedMark','RawManualMark','RawTotalMark']
        writer = csv.DictWriter(outfile,fieldnames=headers)
        writer.writeheader()
        for item in grades.items():
            auto_record = manual_record=''
            if(item[1][0] !=0):
                auto_record = item[1][0]
            if(item[1][1]!=0):
                manual_record = item[1][1]
            writer.writerow({headers[0]:item[0],headers[1]:smart_round(item[1][0],2),headers[2]:smart_round(item[1][1],2),headers[3]:smart_round(item[1][2],2)})



# Do not alter the code below here!
# This is used by the test harness!
# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.
# It's almost the same as in q1.py. Slight change to the default for target and
# updates to the help text.
if __name__ == '__main__':
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Calculate a marks breadown!')
    parser.add_argument('source', type=str, default='exam_for_2020.csv', nargs='?',
                    help='the name of the csv file with grade data to be processed')
    parser.add_argument('target', type=str, default='q3Out.csv', nargs='?',
                    help='the name of the csv file where processed data gets written')

    args = parser.parse_args()

    data = read_data_file(args.source)
    write_report(calculate_marks_breakdown(data), args.target)

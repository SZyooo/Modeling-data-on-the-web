import json
import sys

def evaluate_expr(parsed_expr):
    """This function takes an expression parsed from the JSON
       arithmetic expression format and returns the full evaluation.
       That is, if the JSON expresses '1+1', this function returns '2'."""
    if('root' in parsed_expr):
        return evaluate_expr(parsed_expr['root'])
    else:
        sum = 0
        if('plus' in parsed_expr):
            for exp in parsed_expr['plus']:
                sum += evaluate_expr(exp)
            return sum
        elif('times' in parsed_expr):
            return evaluate_expr(parsed_expr['times'][0]) * evaluate_expr(parsed_expr['times'][1])
        elif('minus' in parsed_expr):
            return evaluate_expr(parsed_expr['minus'][0]) - evaluate_expr(parsed_expr['minus'][1])
        elif('int' in parsed_expr):
            return int(parsed_expr['int'])

def load_json_expr(json_path):
    """This function takes a file path to a JSON file  represened
       as a string and returns a parsed form. You can presume that
       the JSON file is valid wrt the arithmetic expression format."""
    obj = {}
    Json_file = open(json_path, mode = 'r')
    obj = json.load(Json_file)
    Json_file.close()
    return obj
    
# You do not need to touch anything below this line. To complete
# the assignment you need to replace the keyword "pass" in the above
# two functions with code that does the appropriate work.
if __name__=='__main__':
    expr_file_path = sys.argv[1]
    print(evaluate_expr(load_json_expr(expr_file_path)))

# You can run this with "python3 humanReadable.py <path_to_xml_file> <path_to_RelaxNG_file>"
# It only works on RelaxNG schemas in XML syntax, so you may have to translate yours first
#

# Do *NOT* import anything else. You don't need it and if it causes
# your script to fail in our test environment (because we haven't installed
# whatever is) you may lose points.

from lxml import etree

def recersive_operate(root):
    result = ''
    hasParenthesis = True
    if(root.tag == 'expression'):
        result = recersive_operate(root[0])
        result = result[1:-1]
        hasParenthesis = False
    elif(root.tag == 'plus'):
        flag = ''
        for child in root:
            result += flag + recersive_operate(child)
            if(flag == ''):
                flag = '+'
    elif(root.tag == 'times'):
        flag = ''
        for child in root:
            result += flag + recersive_operate(child)
            if(flag == ''):
                flag = '*'
    elif(root.tag == 'minus'):
        result += recersive_operate(root[0]) + '-' + recersive_operate(root[1])
    elif(root.tag == 'int'):
        result = root.attrib['value']
        hasParenthesis = False
    if(hasParenthesis == True):
        result = '(' + result + ')'
    
    return result

def convert_to_readable(source):
    '''This takes a valid XML arithmetical expression and
    returns a "human readable" version. We count a string
    as human readable if is an executable Python arithmetic
    expression which is isomorphic to the XML and evaluates
    to the same answer'''
    tree = etree.parse(source)
    root = tree.getroot()
    result = recersive_operate(root)
    return result # This is a dummy value!


# Do not alter the code below here!
# This is used by the test harness!
# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.

if __name__ == '__main__':
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Translate a valid XML expression into normal Python arithmetic')
    parser.add_argument('source', type=str, default='example.xml', nargs='?',
                    help='the name of the xml file with the arithmetic expression')

    args = parser.parse_args()

    print(convert_to_readable(args.source))

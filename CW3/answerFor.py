# You can run this with "python3 answerFor.py <path_to_xml_file> <path_to_RelaxNG_file>" 
# It only works on RelaxNG schemas in XML syntax, so you may have to translate yours first

from lxml import etree

def well_formed(source):
    '''This function takes a filepath to a *well-formed* XML file
    and  the other to a RELAXNG schema in XML syntax. This function returns
    True if  the XML file is well-formed and False otherwise.'''
    result = True
    try:
        f = open(source,'r')
        _str = f.read()
        data = bytes(_str, encoding='utf-8')
        doc = etree.fromstring(data)
    except etree.XMLSyntaxError as e:
        result = False

    return result # This is a DUMMY ANSWER
    
def valid(source, schema):
    '''This function takes two filepaths, one to a *well-formed* XML file
    and  the other to a RELAXNG schema in XML syntax. This function returns
    True if  the XML file is valid wrt the schema and False otherwise.'''
    xml_file = etree.parse(source)
    xml_validator = etree.RelaxNG(file=schema)

    is_valid = xml_validator.validate(xml_file)
    return is_valid # This is a DUMMY ANSWER

def recersive_operate(root):
    result = 0
    if(root.tag == 'expression'):
        result = recersive_operate(root[0])
    elif(root.tag == 'plus'):
        for child in root:
            result += recersive_operate(child)
    elif(root.tag == 'times'):
        result = 1
        for child in root:
            result *= recersive_operate(child)
    elif(root.tag == 'minus'):
        result = recersive_operate(root[0]) - recersive_operate(root[1])
    elif(root.tag == 'int'):
        result = int(root.attrib['value'])
    return round(result,2)

def evaluate(source):
    '''This takes a valid XML arithmetical expression evaluates
    it to a integer.'''
    tree = etree.parse(source)
    root = tree.getroot()
    result = recersive_operate(root)
    return result
    
    
# Do not alter the code below here!
# This is used by the test harness!

def check_then_evaluate(source, schema):
    if not well_formed(source): 
        return 'Not well formed'
        
    if not valid(source, schema):
        return 'Not valid' 

    # This will only return if you pass both tests
    
    return evaluate(source)


# If you are interested in how it works, read the module documentation for argparse.
# argparse makes writing reasonably robust command line tools pretty easy.

if __name__ == '__main__':
    import sys
    print(sys.path[4])
    # Importing here is not standard, but convenient for this assignment.
    import argparse
    parser = argparse.ArgumentParser(description='Check a calc format file for validatity and evaluated it if it is valid.')
    parser.add_argument('source', type=str, default='test1.xml', nargs='?',
                    help='the name of the xml file with the arithmetic expression')
    parser.add_argument('--schema', '-s', type=str, default='calc1.rng',
                    help='the name of RELAXNG scheme (in XML syntax)')

    args = parser.parse_args()

    print(check_then_evaluate(args.source, args.schema))

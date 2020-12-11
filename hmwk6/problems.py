import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    targetSearch = r'^\(?\d?\d?\d?\)?\-?\s?\d\d\d\-\d\d\d\d$'
    x = re.search(targetSearch, searchstring)

    if not x:
        return False
    else:
        return True
    pass
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    pattern = r'\d+\s(?P<x>[\w\W]+)(\sRd|\sDr|\sAve|\sSt)'
    x = re.findall(pattern, searchstring)

    return x[0][0]
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    pattern = r'\d+\s(?P<x>[\w\W]+)(\sRd|\sDr|\sAve|\sSt)'
    x = re.findall(pattern, searchstring)
    str_to_reverse = x[0][0]
    str_to_put_back = str_to_reverse[::-1]

    retStr = searchstring.replace(str_to_reverse, str_to_put_back)

    return retStr


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))

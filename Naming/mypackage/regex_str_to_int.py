import re

def special_match(strg, search=re.compile(r'[^0-9&(,.|.|,|)]').search):
    '''
    :param strg: the string
    :param search: should have !!!!only!!!! [0-9] and ( ,. or , or . or '' )
    :return: True or False
    '''
    return not bool(search(strg))

def get_str_from_separated_list(x,separ):
    '''

    :param x: list
    :param separ: ',' or '.'
    :return: integer part
    '''
    list1 = x.split(separ);
    new_str = ''
    if len(list1) > 2:
        for i in range(len(list1) - 2): new_str += list1[i]
    else:
        new_str = list1[0]
    if new_str=='': return 0
    return int(new_str)

def separ_str(x):
    '''

    :param x:
    :return: separator of x
    '''
    separ = '.'
    if ',' in x: separ = ','

    return separ

def str_to_int(x):
    '''

    :param x:
    if x starts with + or - : x becomes x[1:]
    :return: integer part of x

    if x has anything else besides [0-9,.] return 0
    if x starts with , or . return 0
    '''
    if type(x) == str:
        if x[0] == '(' and x[len(x)-1] == ')':  x = x.replace(')','').replace('(','').replace(', ',',')

    if x[0] == '-' or x[0] == '+': x = x[1:]

    if special_match(x):
        if x[0] in ',.': return 0

        if ('.' in x and ',' not in x) or ('.' not in x and ',' in x):
            separ = separ_str(x)
            return get_str_from_separated_list(x,separ)

        elif '.' in x or ',' in x:
            for i in range(len(x)-1,0,-1):
                if x[i] in ',.': break
            if x[i] == ',':
                x=x.replace('.', '')
            else:
                x=x.replace(',', '')
            separ = separ_str(x); return get_str_from_separated_list(x, separ)

        return int(x)

    return 0

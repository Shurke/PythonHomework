import sys
import math


CONSTANTS = ('pi', 'tau', 'e', 'inf', 'nan')
OPERATORS = ('+', '-', '*', '/', '//', '%', '^', '<', '<=', '==', '!=', '>=', '>', '(', 'neg', 'pos')

def get_token(input_expression):
    if input_expression.count('(') != input_expression.count(')'):
        print('ERROR: the number of opening and closing brackets must match')
        sys.exit(1)
    else:
        token = ['']
        for i in input_expression:
            if i.isdigit() and token[-1].isdigit():
                token[-1] = token[-1]+i
            elif i == '.' and token[-1].isdigit():
                token[-1] = token[-1] + i
            elif i.isdigit() and '.' in token[-1]:
                token[-1] = token[-1] + i
            elif i.isalpha() and token[-1].isalpha():
                token[-1] = token[-1] + i
            elif i == '/' and token[-1] == '/':
                token[-1] = token[-1] + i
            elif i == '=' and token[-1] in '<>!=':
                token[-1] = token[-1] + i
            else:
                token.append(i)

        tokens = token[1:]
        infix = ['']
        while tokens:
            x = tokens[0]
            tokens = tokens[1:]
            if x in CONSTANTS:
                infix.append(math.__dict__[x])
            elif x == '-' and (infix[-1] == '' or infix[-1] in OPERATORS):
                infix.append('neg')
            elif x == '+' and (infix[-1] == '' or infix[-1] in OPERATORS):
                infix.append('pos')
            elif x.isnumeric():
                infix.append(float(x))
            else:
                infix.append(x)
    return infix[1:]

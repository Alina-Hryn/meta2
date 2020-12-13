import re

file_extension = '.rb'
uppercase_words_part = ('HTTP', 'RFC', 'XML', 'HTML')
keywords = ('__ENCODING__', '__LINE__', '__FILE__', 'BEGIN', 'END', 'alias', 'and', 'begin', 'break',
            'case', 'defined?', 'do', 'else', 'elsif', 'end', 'ensure', 'false', 'for',
            'if', 'in', 'module', 'next', 'nil', 'not', 'or', 'redo', 'rescue', 'retry', 'return', 'self',
            'super', 'then', 'true', 'undef', 'unless', 'until', 'when', 'while', 'yield')
operators = ('eql?', 'equal?', '==', '=', '!=', '<', '<=', '>', '>=', '+', '+', '-', '*', '/', '**', '==',
             '>', '<', '|', '&', '^', '<<', '[]', '===')

punctuation = ('[', ']', '(', ')', ',', ';', '::', ':', '.', '{', '}', '\0')


def is_keyword(token):
    if token in keywords:
        return True
    return False


def is_operator(token):
    if token.lower() in operators:
        return True
    return False


def is_ruby_file(name):
    if name.endswith(file_extension):
        return True
    return False


def get_list_from_line(line):
    for operator in operators:
        line = line.replace(operator, ' ' + operator + ' ')
    # for punct in punctuation:
    #     line = line.replace(punct, ' ' + punct + ' ')
    line = re.sub("^(\s)+", " ", line)
    line = line.split(' ')
    line = list(filter(None, line))
    return line


def get_string_from_list(lexemes):
    return ''.join(lexemes)

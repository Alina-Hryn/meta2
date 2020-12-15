import re

file_extension = '.rb'
uppercase_words_part = ('HTTP', 'RFC', 'XML', 'HTML')
keywords = ('__ENCODING__', '__LINE__', '__FILE__', 'BEGIN', 'END', 'alias', 'and', 'begin', 'break',
            'case', 'defined?', 'do', 'else', 'elsif', 'end', 'ensure', 'false', 'for',
            'if', 'in', 'module', 'next', 'nil', 'not', 'or', 'redo', 'rescue', 'retry', 'return', 'self',
            'super', 'then', 'true', 'undef', 'unless', 'until', 'when', 'while', 'yield')
operators = ('eql?', 'equal?', '==', '=', '!=', '<', '<=', '>', '>=', '+', '+', '-', '*', '/', '**', '==',
             '>', '<', '|', '&', '^', '<<', '[]', '===')

punctuation = ('[', ']', '(', ')', ',', ';', '.', '{', '}', '\0')

annotations = {
    'TokenType.METHOD': ['def', "#Annotation before def"],
    'TokenType.CLASS': ['class', "#Annotation before class"]
}


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
    for punct in punctuation:
        line = line.replace(punct, ' ' + punct + ' ')
    line = re.sub("^(\s)+", " ", line)
    line = line.split(' ')
    line = list(filter(None, line))
    return line


def get_file_from_list(list):
    return '\n'.join(list)


def diff(li1, li2):
    return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))


def get_folder_names(f1, f2):
    f1 = f1.replace('\\', '/')
    f1 = f1.split('/')
    f2 = f2.replace('\\', '/')
    f2 = f2.split('/')[:-1]
    return diff(f1, f2)

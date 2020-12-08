file_extension = '.rb'
uppercase_words_part = ('HTTP', 'RFC', 'XML')
keywords = ('__ENCODING__', '__LINE__', '__FILE__', 'BEGIN', 'END', 'alias', 'and', 'begin', 'break',
            'case', 'class', 'def', 'defined?', 'do', 'else', 'elsif', 'end', 'ensure', 'false', 'for',
            'if', 'in', 'module', 'next', 'nil', 'not', 'or', 'redo', 'rescue', 'retry', 'return', 'self',
            'super', 'then', 'true', 'undef', 'unless', 'until', 'when', 'while', 'yield')
operators = ('=', '==', '!=', '<', '<=', '>', '>=', '+', '+', '-', '*', '/', '**', '==', '>', '<',
             '|', '&', '^', 'eql?', 'equal?', '<<', '[]', '===')

punctuation = ('[', ']', '(', ')', ',', ';', '::', ':', '.', '?', '{', '}', '\0')


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


def is_snake_case(token):
    if token.islower():
        return True
    else:
        for upper_word in uppercase_words_part:
            if upper_word in token:
                token = token.replace(upper_word, '')
                is_snake_case(token)
        return False


# TODO
def is_camel_case(token):
    if '_' in token:
        return False


def get_list_from_line(line):
    for operator in operators():
        line.replace(operator, ' ' + operator + ' ')
    for punct in punctuation:
        line.replace(punct, ' ' + punct + ' ')
    return line.strip(' ')


def get_line_from_list(lexemes):
    return ' '.join(lexemes)

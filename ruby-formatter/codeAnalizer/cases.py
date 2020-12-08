file_extension = '.rb'
uppercase_words_part = ('HTTP', 'RFC', 'XML')
keywords = ('__ENCODING__', '__LINE__', '__FILE__', 'BEGIN', 'END', 'alias', 'and', 'begin', 'break',
            'case', 'class', 'def', 'defined?', 'do', 'else', 'elsif', 'end', 'ensure', 'false', 'for',
            'if', 'in', 'module', 'next', 'nil', 'not', 'or', 'redo', 'rescue', 'retry', 'return', 'self',
            'super', 'then', 'true', 'undef', 'unless', 'until', 'when', 'while', 'yield')
operators = ('=', '==', '!=', '<', '<=', '>', '>=', '+', '+', '-', '*', '/', '**', '==', '>', '<',
             '|', '&', '^', 'eql?', 'equal?', '<<', '[]', '===')


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


def is_camel_case(token):
    if '_' in token:
        return False

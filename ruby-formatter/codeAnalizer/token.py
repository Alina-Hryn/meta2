import re
from enum import Enum

from codeAnalizer.cases import uppercase_words_part


class TokenType(Enum):
    CLASS = 1
    VAR = 2
    METHOD = 3
    CONSTRAINT = 3


class Token:
    def __init__(self, value, token_type, definition):
        self.value = value
        self.new_value = ""
        self.token_type = token_type
        self.definition = definition

    def make_camel_case(self):
        new_value = self.value[0].upper()
        i = 1
        while i < len(self.value):
            if self.value[i] == '_':
                i += 1
                continue
            if self.value[i - 1] == '_':
                new_value += self.value[i].upper()
            else:
                new_value += self.value[i]
            i += 1
        self.new_value = new_value

    def make_snake_case(self):
        new_value = self.value[0].lower()
        i = 1
        while i < len(self.value):
            if self.value[i].isupper():
                new_value += '_' + self.value[i].swapcase()
                i += 1
            if self.value[i - 1] == '_':
                new_value += self.value[i].lower()
            else:
                new_value += self.value[i]
            i += 1
        self.new_value = new_value

    def capitalize_acronyms(self):
        for word in uppercase_words_part:
            if re.search(word, self.new_value, re.IGNORECASE):
                self.new_value = re.sub(word, word.upper(), self.new_value, flags=re.IGNORECASE)

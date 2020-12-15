import re
from enum import Enum

from code_analizer.cases import uppercase_words_part


class TokenType(Enum):
    CLASS = 1
    VAR = 2
    METHOD = 3
    CONSTRAINT = 4
    DEFAULT = 5


class Token:
    def __init__(self, value='', token_type=TokenType.DEFAULT, need_annotation=False):
        self.value = value
        self.new_value = ""
        self.token_type = token_type
        self.need_annotation = need_annotation

    def run(self):
        if self.token_type == TokenType.VAR or self.token_type == TokenType.METHOD:
            self.make_snake_case()
        elif self.token_type == TokenType.CLASS:
            self.make_camel_case()
        else:
            self.new_value = self.value
        self.capitalize_acronyms()

    def make_camel_case(self):
        self.lowcase_acronyms()
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
        new_value = new_value.replace('_', '')
        self.new_value = new_value
        self.capitalize_acronyms()

    def check_method_naming(self):
        words = ['is', 'can', 'does', 'do']
        if self.token_type == TokenType.METHOD:
            for word in words:
                is_w = False
                if self.new_value.startswith(word + '_'):
                    self.new_value = self.new_value.replace(word + '_', '')
                    if not self.value.endswith('?'):
                        self.new_value = self.new_value + '?'

    def make_snake_case(self):
        self.lowcase_acronyms()
        new_value = self.value[0].lower()
        i = 1
        while i < len(self.value):
            if self.value[i].isupper():
                new_value += '_' + self.value[i].swapcase()
                if i < len(self.value) - 1:
                    i += 1
            if self.value[i - 1] == '_':
                new_value += self.value[i].lower()
            else:
                new_value += self.value[i]
            i += 1
        new_value = re.sub("\_+", "_", new_value)
        self.new_value = new_value
        self.capitalize_acronyms()
        self.check_method_naming()

    def capitalize_acronyms(self):
        for word in uppercase_words_part:
            if re.search(word.lower(), self.new_value):
                self.new_value = re.sub(word.lower(), word.upper(), self.new_value)
                print(self.new_value)

    def lowcase_acronyms(self):
        for word in uppercase_words_part:
            if re.search(word, self.value, flags=re.IGNORECASE):
                print(True)
                self.value = re.sub('(?i)' + word, word.lower(), self.value)
                print(self.value)

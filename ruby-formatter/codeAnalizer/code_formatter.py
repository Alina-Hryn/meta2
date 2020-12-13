import re

from code_analizer.code_parser import CodeParser


class CodeFormatter:
    def __init__(self, file_string):
        self.file_string = file_string
        code_parser = CodeParser(file_string)
        self.tokens = code_parser.tokens

    def replace_lexemes_in_file(self):
        for token in self.tokens:
            if token.value != token.new_value:
                self.replace_lexeme_in_file(token.value, token.new_value)
        print(self.file_string)

    def replace_lexeme_in_file(self, lexeme, replaceTo):
        self.file_string = re.sub(r"(?<![0-9a-zA-Z_])(" + lexeme + ")(?![0-9a-zA-Z_])", replaceTo, self.file_string)
        # print(self.file_string)

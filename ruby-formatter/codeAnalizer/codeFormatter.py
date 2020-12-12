import re


class CodeFormatter:
    def __init__(self, file_string):
        self.file_string = file_string

    def replace_lexeme_in_file(self, lexeme, replaceTo):
        self.file_string = re.sub(r"(?<![0-9a-zA-Z_])(" + lexeme + ")(?![0-9a-zA-Z_])", replaceTo, self.file_string)
        print(self.file_string)
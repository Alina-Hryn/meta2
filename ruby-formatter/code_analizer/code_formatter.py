import os
import re

from code_analizer.cases import annotations, file_extension, get_file_from_list
from code_analizer.code_parser import CodeParser
from code_analizer.token import TokenType


class CodeFormatter:
    def __init__(self, file, file_names):
        self.file_string = file.file_string
        code_parser = CodeParser(file.file_string)
        self.modified = file.modified
        self.tokens = code_parser.tokens
        self.file_names = file_names

    @staticmethod
    def run(file, verify, fix, file_names):
        code_formatter = CodeFormatter(file, file_names)
        if verify:
            code_formatter.find_lexeme_in_file()
        if fix:
            code = code_formatter.format_file()
            code = get_file_from_list(code)
            ruby_m = open(code_formatter.modified, 'w')
            ruby_m.write(code)
            ruby_m.close()
            # print(code)

    @staticmethod
    def screen_lexeme(lexeme):
        lexeme = lexeme.replace('?', '\?')
        lexeme = lexeme.replace('$', '\$')
        return lexeme

    def find_lexeme_in_file(self):
        for token in self.tokens:
            if token.value != token.new_value:
                file_lines = self.file_string.split('\n')
                for n, line in enumerate(file_lines):
                    res = re.search(r"(?<![0-9a-zA-Z_])(" + token.value + ")(?![0-9a-zA-Z_])", line)
                    if res:
                        print(token.value, line, n)

    def format_file(self):
        file_lines = self.file_string.split('\n')
        code = []
        for line in file_lines:
            for token in self.tokens:
                before_replace = CodeFormatter.screen_lexeme(token.new_value)
                if token.value != token.new_value:
                    line = re.sub(
                        r"(?<![0-9a-zA-Z_])(" + CodeFormatter.screen_lexeme(token.value) + ")(?![0-9a-zA-Z_])",
                        token.new_value, line)
                if token.need_annotation:
                    comment = annotations[str(token.token_type)][1] + ' ' + token.new_value + '\n'
                    line = re.sub("(?<=^)([\t\s]*)(" + annotations[str(token.token_type)][0]
                              + ".*(?<![a-zA-Z0-9_])" + token.new_value + "(?![a-zA-Z0-9_]))", r"\1" + comment + r"\1\2", line)

            code.append(line)
        return code

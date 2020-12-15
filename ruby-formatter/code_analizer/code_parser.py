from code_analizer.cases import get_list_from_line, keywords, punctuation, is_keyword
import re

from code_analizer.token import Token, TokenType


class CodeParser:
    def __init__(self, file_string):
        self.file_string = file_string
        self.lines = []
        self.lexemes = []
        self.tokens = []
        self.make_lexems()

    def make_lexems(self):
        self.remove_comments()
        self.make_list_from_file()
        for id, line in enumerate(self.lines):
            self.lexemes.append(get_list_from_line(line))
            prev_line = [] if len(self.lexemes) == 1 else self.lexemes[-2]
            token = self.search_incorrect_lexeme(self.lexemes[-1], prev_line)
            if token is not None:
                token.run()
                self.tokens.append(token)
            # print(line)
        print(self.lexemes)

    def search_incorrect_lexeme(self, line, prev_line):
        token = Token()
        token_type = None
        if line[0].lower() == 'def':
            result = re.match('^[a-zA-Z_][a-zA-Z0-9_]*(!|\?)?$', line[1])
            if result:
                value = line[1]
                token_type = TokenType.METHOD
        elif line[0].lower() == 'class':
            result = re.match('^[a-zA-Z_][a-zA-Z0-9]*$', line[1])
            if result:
                    value = line[1]
                    token_type = TokenType.CLASS
        else:
            result = re.match('^(\@\@?|\$)?[a-zA-Z_][a-zA-Z0-9_]*$', line[0])
            if not is_keyword(line[0]):
                if (len(line) == 1 or line[1] == '=') and result:
                    value = line[0]
                    token_type = TokenType.VAR
                    result = re.match('^(\@\@?|\$)?[A-Z][A-Z0-9_]*$', line[0])
                    if result:
                        value = line[0]
                        token_type = TokenType.CONSTRAINT

        if token_type is not None:
            token.value = value
            token.token_type = token_type
            needed = [TokenType.CLASS, TokenType.METHOD]
            if token_type in needed and (not prev_line or prev_line[0] != "'ONE_LINE_COMMENT'"):
                token.need_annotation = True
            return token
        return None

    def remove_comments(self):
        self.file_string = re.sub(r"('.*')|(\".*\")", "'STRING'", self.file_string)
        self.file_string = re.sub(r"=begin(.|\n)+?=end", "'MULTILINE_COMMENT'", self.file_string)
        self.file_string = re.sub(r"#.+", "'ONE_LINE_COMMENT'", self.file_string)
        self.file_string = re.sub(";", "\n", self.file_string)
        self.file_string = re.sub(r"self(::|.)?", "", self.file_string)
        self.file_string = re.sub("^(\s)*", "", self.file_string)

    def make_list_from_file(self):
        self.lines = self.file_string.split('\n')
        self.lines = list(filter(None, self.lines))

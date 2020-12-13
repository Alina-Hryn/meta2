from codeAnalizer.cases import get_list_from_line, keywords, punctuation, is_keyword
import re

from codeAnalizer.token import Token, TokenType


class CodeParser:
    def __init__(self, file_string, lines):
        self.file_string = file_string
        self.lines = lines
        self.lexemes = []
        self.make_lexems()
        self.tokens = []

    def make_lexems(self):
        self.remove_comments()
        self.make_list_from_file()
        for id, line in enumerate(self.lines):
            self.lexemes.append(get_list_from_line(line))
            token = self.search_incorrect_lexeme(self.lexemes[-1])
            if token is not None:
                token.run()
                print('\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(token.new_value))
            print(line)
        print(self.lexemes)

    def search_incorrect_lexeme(self, line):
        token = Token()
        token_type = None
        if line[0].lower() == 'def':
            # result = re.match('^(@@?|$)?[a-zA-Z0-9_]+(\?|!)?$', line[1])
            result = re.match('^[a-z0-9_]+(\?|!)?$', line[1])
            if not result:
                result = re.match('^[a-zA-Z0-9_]+(\?|!)?$', line[1])
                if result:
                    value = line[1]
                    token_type = TokenType.METHOD
                    return token
                    print("OK def")
            else:
                value = line[1]
                token_type = TokenType.METHOD
        elif line[0].lower() == 'class':
            result = re.match('^[a-zA-Z0-9]+$', line[1])
            if not result:
                result = re.match('^[a-zA-Z0-9_]+$', line[1])
                if result:
                    value = line[1]
                    token_type = TokenType.CLASS
                    print('OK class')
            else:
                value = line[1]
                token_type = TokenType.CLASS
        else:
            # print('\t \t \t' + line[0])
            result = re.match('^(\@\@?|\$)?[a-z_][a-z0-9_]*$', line[0])
            if not is_keyword(line[0]):
                if (len(line) == 1 or line[1] == '=') and not result:
                    if not result:
                        result = re.match('^(\@\@?|\$)?[a-zA-Z_][a-zA-Z0-9_]*$', line[0])
                        if result:
                            value = line[0]
                            token_type = TokenType.VAR
                            print('OK var')
                    result = re.match('^(\@\@?|\$)?[A-Z][A-Z0-9_]*$', line[0])
                    if result:
                        value = line[0]
                        token_type = TokenType.CONSTRAINT
                elif (len(line) == 1 or line[1] == '=') and result:
                    value = line[0]
                    token_type = TokenType.VAR
        if token_type != None:
            token.value = value
            token.token_type = token_type
            return token
        return None



    def remove_comments(self):
        self.file_string = re.sub(r"('.*')|(\".*\")", "'STRING'", self.file_string)
        self.file_string = re.sub(r"=begin(.|\n)+?=end", "'MULTILINE_COMMENT'", self.file_string)
        self.file_string = re.sub(r"#.+", "'ONE_LINE_COMMENT'", self.file_string)
        self.file_string = re.sub(";", "\n", self.file_string)
        self.file_string = re.sub(r"self(::|.)?", "", self.file_string)
        self.file_string = re.sub("^(\s)*", "", self.file_string)
        # file_string = self.file_string
        # for k in keywords:
        #     file_string = re.sub(r"(?<![@$0-9a-zA-Z_])(" + k + ")(?![0-9a-zA-Z_!])", '', file_string)
        # for punct in punctuation:
        #     file_string = file_string.replace(punct, '')
        # self.file_string = file_string

    def make_list_from_file(self):
        self.lines = self.file_string.split('\n')
        self.lines = list(filter(None, self.lines))
        # line = line.strip(' ').split(' ')
        # line = list(filter(None, line))

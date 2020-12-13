from codeAnalizer.cases import get_list_from_line, keywords, punctuation, is_keyword
import re


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
        for line in self.lines:
            self.lexemes.append(get_list_from_line(line))
            self.search_incorrect_lexeme(self.lexemes[-1])
            print(line)
        print(self.lexemes)

    def search_incorrect_lexeme(self, line):
        if line[0].lower() == 'def':
            # result = re.match('^(@@?|$)?[a-zA-Z0-9_]+(\?|!)?$', line[1])
            result = re.match('^[a-z0-9_]+(\?|!)?$', line[1])
            if not result:
                result = re.match('^[a-zA-Z0-9_]+(\?|!)?$', line[1])
                if result:
                    print("OK def")
                else:
                    print("OH def")
            else:
                print('DEF!')
        elif line[0].lower() == 'class':
            result = re.match('^[a-zA-Z0-9]+$', line[1])
            if not result:
                result = re.match('^[a-zA-Z0-9_]+$', line[1])
                if result:
                    print('OK class')
                else:
                    print('OH class')
            else:
                print("CLASS")
        else:
            # print('\t \t \t' + line[0])
            result = re.match('^(\@\@?|\$)?[a-z_][a-z0-9_]*$', line[0])
            if not is_keyword(line[0]):
                if result and (len(line) == 1 or line[1] == '='):
                    print("VARIABLE")
                if not result:
                    result = re.match('^(\@\@?|\$)?[a-zA-Z_][a-zA-Z0-9_]*$', line[0])
                    if result:
                        print('OK var')
            elif is_keyword(line[0]):
                print("KEYWORD")


    def remove_comments(self):
        self.file_string = re.sub(r"('.*')|(\".*\")", "'STRING'", self.file_string)
        self.file_string = re.sub(r"=begin(.|\n)+?=end", "'MULTILINE_COMMENT'", self.file_string)
        self.file_string = re.sub(r"#.+", "'ONE_LINE_COMMENT'", self.file_string)
        self.file_string = re.sub(";", "\n", self.file_string)
        self.file_string = re.sub("^(\s)*", "", self.file_string)
        file_string = self.file_string
        # for k in keywords:
        #     file_string = re.sub(r"(?<![@$0-9a-zA-Z_])(" + k + ")(?![0-9a-zA-Z_!])", replaceTo, self.file_string)
        for punct in punctuation:
            file_string = file_string.replace(punct, '')
        self.file_string = file_string

    def make_list_from_file(self):
        self.lines = self.file_string.split('\n')
        self.lines = list(filter(None, self.lines))
        # line = line.strip(' ').split(' ')
        # line = list(filter(None, line))

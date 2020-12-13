from codeAnalizer.cases import get_list_from_line
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
        print(self.lines)
        for line in self.lines:
            self.lexemes.append(get_list_from_line(line))
            self.search_incorrect_lexeme(self.lexemes[-1])
            print(line)
        print(self.lexemes)

    def search_incorrect_lexeme(self, line):
        if line[0].upper() == 'def'.upper():
            print("\t \t \t\t \t \t DEF!")
        elif line[0].upper == 'class'.upper():
            print('\t \t \t\t \t \t CLASS')
        elif line[0][0] == '@':
            print('\t \t \t\t \t \t @')
        elif line[0][0] == '$':
            print('\t \t \t\t \t \t $')
        else:
            print('\t \t \t' + line[0])

    def remove_comments(self):
        self.file_string = re.sub(r"('.*')|(\".*\")", "'STRING'", self.file_string)
        self.file_string = re.sub(r"=begin(.|\n)+?=end", "'MULTILINE_COMMENT'", self.file_string)
        self.file_string = re.sub(r"#.+", "'ONE_LINE_COMMENT'", self.file_string)
        self.file_string = re.sub(";", "\n", self.file_string)

    def make_list_from_file(self):
        self.lines = self.file_string.split('\n')
        self.lines = list(filter(None, self.lines))
        # line = line.strip(' ').split(' ')
        # line = list(filter(None, line))

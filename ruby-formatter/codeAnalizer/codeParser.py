from codeAnalizer.cases import get_list_from_line
import re

class CodeParser:
    def __init__(self, file_string, lines):
        self.file_string = file_string
        self.lines = lines
        self.lexemes = []
        self.make_lexems()

    def make_lexems(self):
        self.remove_comments()
        self.make_list_from_file()
        print(self.lines)
        for line in self.lines:
            self.lexemes.append(get_list_from_line(line))
            print(line)
        print(self.lexemes)

    def remove_comments(self):
        self.file_string = re.sub(r"('.*')|(\".*\")", "'STRING'", self.file_string)
        self.file_string = re.sub(r"=begin(.|\n)+?=end", "'MULTILINE_COMMENT'", self.file_string)
        self.file_string = re.sub(r"#.+", "'ONE_LINE_COMMENT'", self.file_string)

    def make_list_from_file(self):
        self.lines = self.file_string.split('\n')
        self.lines = list(filter(None, self.lines))
        # line = line.strip(' ').split(' ')
        # line = list(filter(None, line))
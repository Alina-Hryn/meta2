import os

from code_analizer.cases import operators, punctuation, file_extension
# from codeAnalizer.codeParser import CodeParser
from code_analizer.code_formatter import CodeFormatter


class FilesParser:
    def __init__(self, file_path=''):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.file_lines = []
        self.read_file()

    def __str__(self):
        print(str(self.file_name))

    def read_file(self):
        if self.check_ruby_file(self.file_path):
            print(self.file_path)
            f = open(self.file_path, "r")
            self.file_string = f.read()
            for line in f:
                self.file_lines.append(line)
                # self.show_line(line)

    def show_file(self):
        for i in self.file_lines:
            print(i)

    def show_line(self, line):
        print(self.file_name + ': ' + line)

    def check_ruby_file(self, file_path):
        if file_path.endswith(file_extension):
            # if file_path.endswith('.groovy'):
            return True
        return False

    @staticmethod
    def get_file(file):
        if os.path.isfile(file):
            file = FilesParser(file)
        return file

    @staticmethod
    def get_directory_files(directory):
        # print(directory)
        directory_files = []
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                file = directory + '/' + file
                if os.path.isfile(file):
                    directory_files.append(FilesParser(file))
        return directory_files

    @staticmethod
    def get_project_files(project, project_files = []):
        if os.path.isdir(project):
            for file in os.listdir(project):
                file = project + '/' + file
                if os.path.isfile(file):
                    project_files.append(FilesParser(file))
                if os.path.isdir(file):
                    FilesParser.get_project_files(file, project_files)
        return project_files


# df = FilesParser.get_project_files('C:/Users/Alina/Desktop/ruby-formatter/meta2/examples')
# df[0].show_file()

# file1 = FilesParser.get_file('C:/Users/Alina/Desktop/ruby-formatter/meta2/examples/example1.rb')
# print(file1.file_lines)
# cp = CodeParser(file1.file_string)

files = FilesParser.get_directory_files("C:/Users/Alina/Desktop/ruby-formatter/meta2/examples")
for file in files:
    print(file.file_string)
    cf = CodeFormatter(file.file_string)


# cf = CodeFormatter(file1.file_string)
# cf.replace_lexeme_in_file('some_method', 'some_m')
# file = FilesParser("C:/Users/Alina/Desktop/ruby-formatter/meta2/examples/example1.rb")


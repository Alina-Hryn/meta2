import os

from code_analizer.cases import operators, punctuation, file_extension
# from codeAnalizer.codeParser import CodeParser
from code_analizer.code_parser import CodeParser


class FilesParser:
    def __init__(self, file_path=''):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.modified = file_path[:-3] + '_modified' + file_extension
        self.file_lines = []
        self.read_file()

    def __str__(self):
        print(str(self.file_path))

    def read_file(self):
        if FilesParser.check_ruby_file(self.file_path):
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

    @staticmethod
    def check_ruby_file(file_path):
        if file_path.endswith(file_extension):
            # if file_path.endswith('.groovy'):
            return True
        return False

    @staticmethod
    def get_file(file):
        file_p =[]
        if os.path.isfile(file) and FilesParser.check_ruby_file(file):
            file_p.append(FilesParser(file))
        else:
            file_p.append(None)
            print("It is not Ruby file! Try again.")
        return file_p

    @staticmethod
    def get_directory_files(directory):
        # print(directory)
        directory_files = []
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                file = directory + '/' + file
                if os.path.isfile(file) and FilesParser.check_ruby_file(file):
                    directory_files.append(FilesParser(file))
        return directory_files

    @staticmethod
    def get_project_files(project, project_files = []):
        if os.path.isdir(project):
            for file in os.listdir(project):
                file = project + '/' + file
                if os.path.isfile(file) and FilesParser.check_ruby_file(file):
                    project_files.append(FilesParser(file))
                if os.path.isdir(file):
                    FilesParser.get_project_files(file, project_files)
        return project_files



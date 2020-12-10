import os

from codeAnalizer.cases import operators, punctuation, file_extension


class FilesParser:
    def __init__(self, file_path=''):
        self.file_path = file_path.replace('\\', '\\\\')
        self.file_name = os.path.basename(self.file_path)
        self.file_lines = []
        self.read_file()

    def __str__(self):
        print(str(self.file_name))

    def read_file(self):
        if self.check_ruby_file(self.file_path):
            print(self.file_path)
            f = open(self.file_path, "r")
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
    def check_directory_files(directory):
        print(directory)
        directory_files = []
        # directory = directory.replace('\\', '\\\\')
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                file = directory + '\\' + file
                if os.path.isfile(file):
                    directory_files.append(FilesParser(file))
        return directory_files

    @staticmethod
    def check_project_files(project, project_files=[]):
        print(project)
        # project_files = []
        # directory = directory.replace('\\', '\\\\')
        if os.path.isdir(project):
            for file in os.listdir(project):
                file = project + '\\' + file
                if os.path.isfile(file):
                    project_files.append(FilesParser(file))
                if os.path.isdir(file):
                    FilesParser.check_project_files(file, project_files)
        return project_files


df = FilesParser.check_project_files(r'C:\Users\Alina\Desktop\ruby-formatter\meta2\examples', [])
print(df)
# f_parser = FilesParser(input('qwerty'))
# f_parser.read_file()
# C:\Users\Alina\Desktop\test.groovy

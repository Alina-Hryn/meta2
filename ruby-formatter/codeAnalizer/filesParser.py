from codeAnalizer.cases import operators, punctuation


class FilesParser:
    def __init__(self):
        self.file_lines = []

    def read_file(self, file_name):
        f = open(file_name, "r")
        print(f.readline())
        for line in f:
            self.file_lines = line



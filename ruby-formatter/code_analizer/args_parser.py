import argparse

from code_analizer.cases import get_file_names
from code_analizer.code_formatter import CodeFormatter
from code_analizer.files_parser import FilesParser


class ArgsParser:
    def __init__(self):
        self.files = []

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description='ruby code analyzer', add_help=True)
        parser.add_argument('-f', '--file', help='check file')
        parser.add_argument('-d', '--directory', help='check directory')
        parser.add_argument('-p', '--project', help='check project')
        parser.add_argument('-fix', help='check files` code convention', action='store_true')
        parser.add_argument('-v', '--verify', help='verify of code correctness', action='store_true')

        args = parser.parse_args()
        args_dictionary = vars(args)
        return args_dictionary

    @staticmethod
    def define_item(my_dict):
        file_path = ''
        verify, fix = False, False
        if my_dict['file'] is not None:
            file_path = my_dict['file']
            files = FilesParser.get_file(file_path)
        if my_dict['directory'] is not None:
            file_path = my_dict['directory']
            files = FilesParser.get_directory_files(file_path)
        if my_dict['project'] is not None:
            file_path = my_dict['project']
            files = FilesParser.get_project_files(file_path)
        if my_dict['verify'] is not None:
            verify = my_dict['verify']

        if my_dict['fix'] is not None:
            fix = my_dict['fix']
        for file in files:
            if file is not None:
                names = get_file_names(file.file_path, file_path)
                print('path:', names)
                cf = CodeFormatter(file, verify, fix, names)

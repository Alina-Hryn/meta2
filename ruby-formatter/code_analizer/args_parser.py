import argparse

from .code_formatter import CodeFormatter
from .files_parser import FilesParser


class ArgsParser:
    def __init__(self):
        self.files = []

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description='ruby code analizer', add_help=True)
        parser.add_argument('-f', '--file', help='check file')
        parser.add_argument('-d', '--directory', help='check directory')
        parser.add_argument('-p', '--project', help='check project')
        parser.add_argument('-fix', help='check files` code convention', action='store_true')
        parser.add_argument('-v', '--verify', help='verify of code correctness', action='store_true')

        args = parser.parse_args()
        args_dictionary = vars(args)
        # print(vars(args).get("directory"))
        # print(vars(args).get("project"))
        # print(vars(args).get("fix"))
        # print(vars(args).get("verify"))
        # print(args_dictionary)
        return args_dictionary

    @staticmethod
    def define_item(my_dict):
        my_list = []

        if my_dict['file'] is not None:
            my_list.append('file')
            my_list.append(my_dict['file'])

        if my_dict['directory'] is not None:
            my_list.append('directory')
            my_list.append(my_dict['directory'])
            files = FilesParser.get_directory_files("C:/Users/Alina/Desktop/ruby-formatter/meta2/examples")
            for file in files:
                print(file.file_string)
                cf = CodeFormatter(file.file_string)

        if my_dict['project'] is not None:
            my_list.append('project')
            my_list.append(my_dict['project'])

        if my_dict['verify'] is not None:
            my_list.append('verify')
            my_list.append(my_dict['verify'])

        if my_dict['fix'] is not None:
            my_list.append('fix')
            my_list.append(my_dict['fix'])

        return my_list


if __name__ == '__main__':
    print('print -h/--help for help')
    a = ArgsParser()
    k = a.parse_args()
    print(k)
    my_list = ArgsParser.define_item(k)
    print(my_list)

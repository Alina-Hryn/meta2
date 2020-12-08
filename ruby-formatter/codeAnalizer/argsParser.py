import argparse


class argsParser:
    pass

    def parse_args(self):
        parser = argparse.ArgumentParser(description='ruby code analizer', add_help=True)
        parser.add_argument('-f', '--file', help='check file')
        parser.add_argument('-d', '--directory', help='check directory')
        parser.add_argument('-p', '--project', help='check project')
        parser.add_argument('-fix', help='check files code convention')
        parser.add_argument('-v', '--verify', help='verify of code correctness', default=True)

        args = parser.parse_args()
        args_dict = vars(args)

        if len(args_dict) == 0:
            print('Wrong usage')
        return args_dict


if __name__ == '__main__':
    print('print -h/--help for help')
    a = argsParser()
    a.parse_args()

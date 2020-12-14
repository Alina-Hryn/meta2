from code_analizer.args_parser import ArgsParser

if __name__ == '__main__':
    print('print -h/--help for help')
    a = ArgsParser()
    k = a.parse_args()
    ArgsParser.define_item(k)
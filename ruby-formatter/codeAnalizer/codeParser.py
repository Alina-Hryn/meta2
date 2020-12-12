from codeAnalizer.cases import get_list_from_line


class CodeParser:
    def __init__(self, lines):
        self.lines = lines
        self.lexemes = []
        self.make_line_to_lexems()

    def make_line_to_lexems(self):
        for line in self.lines:
            self.lexemes.append(get_list_from_line(line))
            # self.tokens.append(line_tokens)
        print(self.lexemes)


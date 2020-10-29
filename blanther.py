#####################
#  TOKENS
#####################

TT_INT = 'INT' # TT - token type
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'


class Token:
    def __init__(self, type_, value):
        self.type = type_ # _ to different from python keyword of type
        self.value = value
    
    def __str__(self):
        if self.value:
            return f'{self.type_}:{self.value}'
        return f'{self.type}'


#####################
#  LEXER
#####################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    def create_tokens(self):
        token = []
        

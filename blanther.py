#####################
#  TOKENS
#####################

class Token:
    def __init__(self, type_, value):
        self.type = type_ # _ to different from python keyword of type
        self.value = value
    
    def __str__(self):
        if self.value:
            return f'{self.type_}:{self.value}'
        return f'{self.type}'

        
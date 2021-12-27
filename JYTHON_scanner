from pylox import tokentype
from pylox.tokentype import TokenType
from pylox import *

class Scanner:
    source: str
    tokens: tuple
    start: int
    current: int
    line: int

    keywords = {
            'if'      : TokenType.IF,
            'or'      : TokenType.OR,
            'and'     : TokenType.AND,
            'Null'     : TokenType.NIL,
            'Def'     : TokenType.FUN,
            'for'     : TokenType.FOR,
            'var'     : TokenType.VAR,
            'True'    : TokenType.TRUE,
            'self'    : TokenType.THIS,
            'else'    : TokenType.ELSE,
            'break'   : TokenType.BREAK,
            'print'   : TokenType.PRINT,
            'super'   : TokenType.SUPER,
            'False'   : TokenType.FALSE,
            'while'   : TokenType.WHILE,
            'class'   : TokenType.CLASS,
            'return'  : TokenType.RETURN,
            'continue': TokenType.CONTINUE
        }
    
    @staticmethod
    # We have staticmethod because final in python doesn't exist sadly
    def _init__(self):
        self.source = "SomeString"
        self.tokens = ()
        self.start = self.current = 0
        self.line = 1
    # EOL condition
    def isAtEnd(self):
        return self.current >= len(self.source)

    def main(self, tokens):
        tokens.scanTokens()
        if self.IsAtEnd:
            return self.current >= len(self.source)
        while not self.IsAtEnd():
            self.start = self.current
            self.scanTokens()
            self.tokens.append("EOF", "NULL", "line")
        return tokens
    #Hops along the stream of characters while reading and consuming them, like a crocodile 
    def advance(self):
        return self.source(self.current+1)
    
    def addToken(self, type:TokenType, literal:object=None):
        text = self.source[self.start:self.current]
        self.tokens.append(type, text, literal, self.line)
    #reading the character but not consuming it
    def peek(self):
        if self.IsAtEnd():
            return '\0'
        return self.source[self.start:self.current]

    def PeekNext(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def IsDigit(self, c):
        return c >= '0' and c <= '9'

    def IsAlpha(self, c):
        return c >= 'a' and c <= 'z' + c >= 'A' and c <= 'Z' + c == '_'

    def IsAlphaNumeric(self, c):
        return self.IsAlpha(c) and self.IsDigit(c)

    def number(self):
        while self.IsDigit(self.peek()):
            self.advance()
            if self.peek() == '.' and self.IsDigit(self.peekNext):
                # Eating up the dot 
                self.advance
            while self.IsDigit(self.peek):
                self.advance()
                self.addToken(TokenType.NUMBER, float(self.source[self.start + 1:self.start - 1]))

    
    def scanToken(self):
        c = self.advance()
        token_getter = self.token_for(c)
        return token_getter()

    def Identifier(self):
        while self.IsAlphaNumeric(self.peek()):
            text = self.source[self.start, self.current]
            type = self.keywords.append(text)
            if type == self.null:
                type = tokentype.IDENTIFIER
                self.addToken(type)

    #For the state machine
    def match(self, ch):
        return self.source[self.current] == ch

    # Imagine python or java without strings, we need those
    def string(self):
        while self.peek() != '"' and not self.IsAtEnd():
            if self.peek() == '\n':
                line = self.line + 1
                self.advance()
            if self.IsAtEnd():
                self.pylox.scan_error(self.line, "unterminated string")
                self.advance()
                value = self.source[self.start + 1:self.current - 1]
                self.addToken(value)




    def token_for(self, c, ch):
        # Lambdas in a state machine make me happy
        match c:
            case '(':
                return lambda: self.add_token(TokenType.LEFT_PAREN)
            case ')':
                return lambda: self.add_token(TokenType.RIGHT_PAREN)
            case '{':
                return lambda: self.add_token(TokenType.LEFT_BRACE)
            case '}':
                return lambda: self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                return lambda: self.add_token(TokenType.COMMA)
            case '.':
                return lambda: self.add_token(TokenType.DOT)
            case '-':
                return lambda: self.add_token(TokenType.MINUS)
            case '+':
                return lambda: self.add_token(TokenType.PLUS)
            case '*':
                return lambda: self.add_token(TokenType.STAR)
            case ';':
                return lambda: self.add_token(TokenType.SEMICOLON)
            case '>':
                return lambda: self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case '=':
                return lambda: self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                return lambda: self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.EQUAL)
            case '!':
                return lambda: self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case 'o':
                if self.match('r'):
                    self.addToken(TokenType.OR)
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            # Ignores whitespace
            case '\n':
                line = self.line + 1
            case '"': 
                self.string()
            # Time for the dreaded slash
            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self.IsAtEnd():
                         self.advance 
                         # 2 backslashes are a comment in java so...
                else:
                    self.addToken(TokenType.SLASH)
            case _:
                if self.IsDigit():
                    self.number()
                elif self.IsAlpha():
                    self.Identifier()
                else:
                    self.pylox.scan_error(self.line, f'"{ch}"unexpected character')
                

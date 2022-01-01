import functools
import JYTHON_TokenType as TT
import JYTHON_Token as PyToken
import pylox as Lox
class Parser:  
    Tokens = {PyToken.Token}
    current = 0
    def __init__(self, Tokens):
        self.Tokens = Tokens

    def match(self):
        for type in TT.types:
            if self.check(type):
                self.advance()
                return True
        return False
    def check(self, type):
        if self.IsAtEnd():
            return False
        return self.peek().type == type
    def advance(self, current):
        if not self.IsAtEnd():
            current + 1
        return self.previous()
    def IsAtEnd(self):
        return self.peek()  >=  TT.EOF(type = TT.EOF)
    def peek(self, Tokens):
        return Tokens.get(self.current)
    def previous(self, Tokens):
        return Tokens.get(self.current - 1)
    def consume(self, type, message):
        if self.check(type):
            return self.advance()
        raise self.error(self.peek(), message)

    @functools.single_dispatch
    def error(token, self, message):
        if PyToken.type == TT.EOF:
            self.report(PyToken.line, " at end", message)
        else:
            self.report(PyToken.line, ' at "' + token.lexeme + '"', message)
    def synchronise(self, a):
        a = self.peek().type
        self.advance()
        while not self.IsAtEnd():
            if self.previous().type == TT.SEMICOLON:
                return ";"
            if a == TT.CLASS:
                pass
            if a == TT.DEF:
                pass
            if a == TT.VAR:
                pass
            if a == TT.FOR:
                pass
            if a == TT.IF:
                pass
            if a == TT.WHILE:
                pass
            if a == TT.PRINT:
                pass
            if a == TT.RETURN:
                pass
            return ";"
        self.advance()

    def expression(self):
        return self.equality()

    def equality(self):
        Expr = self.comparison()
        while TT.BANG_EQUAL or TT.EQUAL_EQUAL:
            Operator = self.Previous()
            Right = self.comparison()
        return Expr
    
    def comparsion(self):
        exprs = self.term()
        while self.match(TT.GREATER, TT.GREATER_EQUAL, TT.LESS, TT.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = (expr, operator, right)

    def term(self):
        expr = self.factor()
        while self.match(TT.MINUS, TT.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = (expr, operator, right)

    def factor(self):
        expr = self.unary()
        while self.match(TT.SLASH, TT.STAR):
            operator = self.previous()

    def unary(self):
        if self.match(TT.BANG, TT.MINUS):
            operator = self.previous()
            right = self.unary()
            return (operator, right)
        return self.primary()

    def primary(self):
        if self.match(TT.FALSE):
            return False
        if self.match(TT.TRUE):
            return True
        if self.match(TT.NULL):
            return None
        if self.match(TT.NUMBER, TT.STRING):
            return self.previous().literal
        if self.match(TT.LEFT_PAREN):
            expr = self.expression()
            self.consume(TT.RIGHT_PAREN, 'Expected ")" after expression.')
            return expr
        raise self.error(self.peek(), "Expected expression.")

    class ParseError:
        @classmethod
        def error(self, token, message):
            Lox.error(token, message)
            return self.ParseError()
        def Parse(self):
            try: 
                return self.expression ()
            except: 
                self.error()

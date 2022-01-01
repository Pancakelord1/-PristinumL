import sys
import pathlib
from pylox.scanner import *
import JYTHON_generateAST
class REPL:
    hadError = False
    def Main(self):
        if len(sys.argv) > 1:
            print("Usage: pylox [script]")
            sys.exit(64)
        elif len(sys.argv) == 1:
            self.RunFile(sys.argv[0])
        else:
            self.RunPrompt()

    def RunFile(self,path):
        bytes = pathlib.Path(path).read_bytes()
        self.Run(bytes.decode())
        if self.hadError == True:
            sys.exit(65)
            
    def RunPrompt(self):
        hadError = False
        while True:
            line = input("PrestiniumL $>| ")
            if not line: break
            self.Run(line)
 
    def Run(self, source: str):
        tokens = Scanner(source).scan_tokens()
        Parser = (tokens)
        expression = Parser.parse 
        if self.hadError():
            return print(JYTHON_generateAST.print(expression))

    def report(self,line: int, where: str, message: str):
        print(f"[line {line}], Error at {where}: {message}", file=sys.stderr)
        hadError = True
        def error(line: int, message: str):
            self.report(line, "", message)

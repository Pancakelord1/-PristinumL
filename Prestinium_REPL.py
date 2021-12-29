import sys
import pathlib
from pylox.scanner import *
class REPL:
    hadError = False
    def Main():
        if len(sys.argv) > 1:
            print("Usage: pylox [script]")
            sys.exit(64)
        elif len(sys.argv) == 1:
            RunFile(sys.argv[0])
        else:
            RunPrompt()

    def RunFile(path):
        bytes = pathlib.Path(path).read_bytes()
        Run(bytes.decode())
        if hadError == True:
            sys.exit(65)
            
    def RunPrompt():
        hadError = False
        while True:
            line = input("JYTHON$| ")
            if not line: break
            Run(line)
 
    def Run(source: str):
        tokens = Scanner(source).scan_tokens()
        for token in tokens:
            print(token)

    def report(line: int, where: str, message: str):
        print(f"[line {line}], Error at {where}: {message}", file=sys.stderr)
        hadError = True
        def error(line: int, message: str):
            report(line, "", message)

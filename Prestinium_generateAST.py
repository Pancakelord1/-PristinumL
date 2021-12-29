import sys
import types
from typing import List
class generateAST:
    def main(self):
        if len(sys.argv) != 1:
            print("Usage: generate_ast <output directory>")
            sys.exit(64)
        OutputDir = sys.argv[0]
        self.defineAST(OutputDir, "exprs", List("Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Object value",
        "Unary    : Token operator, Expr right"))
    
    def defineAST(self, OutputDir, BaseName):
        Path = OutputDir + "\\" + BaseName + ".py"
        with open(Path, "w", encoding="UTF-8") as writer:
            writer.write("class" + BaseName + ":")
        for type in types:
            ClassName = type.split(":", [0])
            Fields = type.split(":", [1])
            self.DefineType(writer, BaseName, ClassName, Fields)
        
    def DefineVisitor(self, writer, BaseName, types):
        writer.write("""
        class Visitor(ABC):
            @abstractmethod
            def visit(self, Visitor):
                pass
            class MyVisitor(Visitor):
                def visit(self, Visitor):
                    pass
                def accept(self, visitor):
                    return visitor.visit
        """)
        for type in types:
            TypeName = type.split(":", [0])
        
    def DefineType(self, writer, BaseName, ClassName, FieldList):
        writer.write("from abc import abstractmethod, ABC")
        writer.write("class" + ClassName + "(" + BaseName + ")" + ":")
        writer.write("    " + ClassName + "(" + FieldList + ")" + ":")
        Fields = FieldList.split(", ")
        for Field in Fields:
            Name = Field.split(" ", [1])
            writer.writer("      self." + Name + " = " + Name)
            self.DefineVisitor(writer, BaseName, types)

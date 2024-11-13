import sys 
from antlr4 import *
from mydsl.MyDSLLexer import MyDSLLexer
from mydsl.MyDSLParser import MyDSLParser

class EvalVisitor(ParseTreeVisitor):
    def visitExpression(self, ctx):
        print(f"Visiting expression: {ctx.getText()}")  # Debugging line
        left = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2 * i - 1).getText()  # Get operator
            right = self.visit(ctx.term(i))
            print(f"Left term: {left}, Operator: {op}, Right term: {right}")
            if op == '+':
                left += right
            elif op == '-':
                left -= right
        return left

    def visitTerm(self, ctx):
        print(f"Visiting term: {ctx.getText()}")  # Debugging line
        left = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()  # Get operator
            right = self.visit(ctx.factor(i))
            print(f"Left factor: {left}, Operator: {op}, Right factor: {right}")
            if op == '*':
                left *= right
            elif op == '/':
                left /= right
        return left

    def visitFactor(self, ctx):
        print(f"Visiting factor: {ctx.getText()}")  # Linha de depuração
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.expression():  # Verifica a expressão dentro de parênteses
            return self.visit(ctx.expression())
        else:
            raise Exception(f"Unrecognized factor: {ctx.getText()}")

def main():
    print("Running main.py...")
    input_stream = InputStream('2 + 3 * (4 - 1)')  # Exemplo de expressão
    lexer = MyDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyDSLParser(stream)
    tree = parser.expression()  # Supondo que 'expression' é a regra inicial
    
    print(tree.toStringTree(recog=parser))  # Depuração da árvore gerada
    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
    main()
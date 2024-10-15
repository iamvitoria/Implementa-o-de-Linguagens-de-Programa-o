# evaluator.py
import sys
import os

from antlr4 import *
from generated.SimpleMathLexer import SimpleMathLexer
from generated.SimpleMathParser import SimpleMathParser
from generated.SimpleMathVisitor import SimpleMathVisitor

class SimpleMathEvaluator(SimpleMathVisitor):
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            return left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

def main():
    # Adicionar o diretório 'generated' ao sys.path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'generated'))

    while True:
        try:
            expression = input("Digite uma expressão matemática (ou 'sair' para encerrar): ")
            if expression.lower() == 'sair':
                break
            input_stream = InputStream(expression)
            lexer = SimpleMathLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = SimpleMathParser(stream)
            tree = parser.expr()
            evaluator = SimpleMathEvaluator()
            result = evaluator.visit(tree)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == '__main__':
        main()
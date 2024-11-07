import sys
from antlr4 import *
from mydsl.MyDSLLexer import MyDSLLexer
from mydsl.MyDSLParser import MyDSLParser

class EvalVisitor(ParseTreeVisitor):
    def visitExpression(self, ctx):
        left = self.visit(ctx.term(0))
        print(f"Left term: {left}")  # Debugging line
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.term(i))
            print(f"Right term: {right}, Operator: {op}")  # Debugging line
            if op == '+':
                left += right
            elif op == '-':
                left -= right
        return left

    def visitTerm(self, ctx):
        left = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))
            if op == '*':
                left *= right
            elif op == '/':
                left /= right
        return left

    def visitFactor(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.LPAREN():  # For expressions in parentheses
            return self.visit(ctx.expression())
        else:
            raise Exception(f"Unrecognized factor: {ctx.getText()}")

def main():
    print("Running main.py...")
    input_stream = InputStream('2 + 3 * (4 - 1)')  # Example expression
    lexer = MyDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyDSLParser(stream)
    tree = parser.expression()  # Assuming 'expression' is your starting rule
    
    print(tree.toStringTree(recog=parser))  # Debugging the tree structure
    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
    main()

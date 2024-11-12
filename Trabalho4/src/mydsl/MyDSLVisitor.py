# Generated from grammar/MyDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyDSLParser import MyDSLParser
else:
    from MyDSLParser import MyDSLParser

# This class defines a complete generic visitor for a parse tree produced by MyDSLParser.

class MyDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyDSLParser#expression.
    def visitExpression(self, ctx:MyDSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#term.
    def visitTerm(self, ctx:MyDSLParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#factor.
    def visitFactor(self, ctx:MyDSLParser.FactorContext):
        return self.visitChildren(ctx)



del MyDSLParser
# Generated from grammar/MyDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyDSLParser import MyDSLParser
else:
    from MyDSLParser import MyDSLParser

# This class defines a complete listener for a parse tree produced by MyDSLParser.
class MyDSLListener(ParseTreeListener):

    # Enter a parse tree produced by MyDSLParser#expression.
    def enterExpression(self, ctx:MyDSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyDSLParser#expression.
    def exitExpression(self, ctx:MyDSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyDSLParser#term.
    def enterTerm(self, ctx:MyDSLParser.TermContext):
        pass

    # Exit a parse tree produced by MyDSLParser#term.
    def exitTerm(self, ctx:MyDSLParser.TermContext):
        pass


    # Enter a parse tree produced by MyDSLParser#factor.
    def enterFactor(self, ctx:MyDSLParser.FactorContext):
        pass

    # Exit a parse tree produced by MyDSLParser#factor.
    def exitFactor(self, ctx:MyDSLParser.FactorContext):
        pass



del MyDSLParser
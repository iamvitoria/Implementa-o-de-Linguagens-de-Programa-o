# Generated from grammar/MyDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,30,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,
        1,2,3,2,28,8,2,1,2,0,0,3,0,2,4,0,2,1,0,1,2,1,0,3,4,29,0,6,1,0,0,
        0,2,14,1,0,0,0,4,27,1,0,0,0,6,11,3,2,1,0,7,8,7,0,0,0,8,10,3,2,1,
        0,9,7,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,
        0,0,13,11,1,0,0,0,14,19,3,4,2,0,15,16,7,1,0,0,16,18,3,4,2,0,17,15,
        1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,0,21,
        19,1,0,0,0,22,28,5,7,0,0,23,24,5,5,0,0,24,25,3,0,0,0,25,26,5,6,0,
        0,26,28,1,0,0,0,27,22,1,0,0,0,27,23,1,0,0,0,28,5,1,0,0,0,3,11,19,
        27
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", 
                      "RPAREN", "INT", "WS" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expression", "term", "factor" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    LPAREN=5
    RPAREN=6
    INT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.TermContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.PLUS)
            else:
                return self.getToken(MyDSLParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.MINUS)
            else:
                return self.getToken(MyDSLParser.MINUS, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MyDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.term()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self.term()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.FactorContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.MUL)
            else:
                return self.getToken(MyDSLParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.DIV)
            else:
                return self.getToken(MyDSLParser.DIV, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MyDSLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.factor()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.factor()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyDSLParser.INT, 0)

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MyDSLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(MyDSLParser.INT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(MyDSLParser.LPAREN)
                self.state = 24
                self.expression()
                self.state = 25
                self.match(MyDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






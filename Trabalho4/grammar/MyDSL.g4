grammar MyDSL;

expression: term ((PLUS | MINUS) term)* ;
term: factor ((MUL | DIV) factor)* ;
factor: INT | LPAREN expression RPAREN ;

PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;

grammar MyDSL;

expression
   : term ((PLUS | MINUS) term)*;
term      : factor (( '*' | '/' ) factor)* ;
factor    : INT | '(' expression ')' ;

INT       : [0-9]+ ;
WS        : [ \t\r\n]+ -> skip ;  // Ignora espaços em branco
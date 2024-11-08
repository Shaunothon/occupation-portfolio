public class interpreter {
    
}
// Revised File
grammar amended;

start:
    expression EOF
   ;

// context-free grammars
  expression
    :
    |   INT | NUMBER
    |   (COMMENTS | MLCOMMENTS)
    |   WHITESPACE
    |   BOOLEAN
    |   VAR ASSIGNMENTOP expression
    |   expression EQUALITYCOMP expression
    |   expression (MULTIPLY | DIVIDE) expression
    |   expression (PLUS | MINUS) expression
    |   LPAREN expression RPAREN expression
    |   LBRACKET expression RBRACKET expression
    |   (STRING | STRING expression)
    |   expression (LESSTOE | MORETOE) expression
    |   IF expression // I only changed these
    |   ELSEIF expression // in this document
    |   ELSE LBRACKET expression RBRACKET // because this way is easier
    |   LOOP VAR (UPTO | IN) (VAR | INT)  COLON STARTBODY expression ENDBODY
    |   CHAR
    |   (VAR | VAR expression)
    |   ARRAY
    |
    ;
// Keywords are difficult to implement and evaluate to VAR (variable).
// Therfore, I need to get creative with reserved word names

// lexer rules
   MULTIPLY :   '*';
   DIVIDE   :   '/';
   PLUS     :   '+';
   MINUS    :   '-';
   INT      :   '0'..'9'+;
   NUMBER   : ('0'..'9'+)'.'('0'..'9'+) | '.'('0'..'9'+);
   BOOLEAN  :   'TRUE' | 'FALSE' | 'True' | 'False';
   WHITESPACE: [ \t\r\n]+ -> skip;
   COMMENTS: '//' ~[\r\n]+ -> skip;  // single line
   MLCOMMENTS: '/*' .*? '*/'-> skip;
   LPAREN: '(';
   RPAREN: ')';
   IF: 'if';
   ELSEIF: 'elseif';
   ELSE: 'else';
   LBRACKET: '{';
   RBRACKET: '}';
   COLON: ':';  // syntax for end of loop header
   STARTBODY:'-''-''-';  // syntax for start of forloop body
   ENDBODY: '@';  //syntax for end of forloop body
   ASSIGNMENTOP: '=';
   EQUALITYCOMP: '==';
   LESSTOE: '<'| '<=';
   MORETOE: '>'| '>=';
   STRING: '"'[a-zA-Z. ]+'"';
   VAR: [a-zA-Z]+;
   CHAR: [a-zA-Z];
   LOOP: '4L';  // for(...)
   IN: 'in2';  // 'into' for example in list[80]
   UPTO: '^2';  // 'upto' for example i < 50 (upto 50)
   ARRAYSUBL:'[';
   ARRAYSUBR: ']';
   ARRAY: VAR '[' (VAR | INT) ']';

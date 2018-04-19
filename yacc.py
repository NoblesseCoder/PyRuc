import ply.yacc as yacc

from Lexical_Analyzer import tokens
import Lexical_Analyzer
precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'times', 'divide'),
)

def p_BLOCKSTMT(p): 
	'''BLOCKSTMT : STMT newline BLOCKSTMT
	| STMT BLOCKSTMT	
	| STMT newline
	| STMT
	'''
def p_STMT(p):
	'''STMT : ASSGN
	| SELECT
	| ITER
	'''
def p_SELECT(p):
	'''SELECT : if EXPR then_tok BLOCKSTMT ELSIF ELSE end
	'''

def p_ELSIF(p):
	'''ELSIF : elsif EXPR then_tok BLOCKSTMT
	|
	'''
def p_ELSE(p):
	'''ELSE : else BLOCKSTMT
	|
	'''
def p_ASSGN(p):
	'''ASSGN : LHS equals EXPR
	'''

def p_LHS(p):
	'''LHS : name
	'''

def p_EXPR(p):
	'''EXPR : EXPR plus EXPR
	| EXPR minus EXPR
	| EXPR times EXPR
	| EXPR divide EXPR
	| EXPR less EXPR
	| EXPR equals equals EXPR
	| EXPR great EXPR
	| EXPR great equals EXPR
	| EXPR less equals EXPR
	| name
	| number
	'''
def p_ITER(p):
	'''ITER : while EXPR do BLOCKSTMT end
	'''

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()




# Build the parser
parser = yacc.yacc(debug=True)

s = open('ruby_test.rb','r').read()

result = parser.parse(s,debug=log)
print(log)
if result is not None:#
	print(result)
print(Lexical_Analyzer.symbol_table)

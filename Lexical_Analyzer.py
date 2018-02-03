# Python program to do Lexical Analysis of Ruby code.
import ply.lex as lex
import re
#	Ruby Token List
tokens=('NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN',
	'RPAREN','COMMENT','KEYWORDS','APPEND','TERMINATOR','STRING')

#	RegEx for simple tokens
t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_EQUALS=r'='
t_APPEND=r'<<'
t_TERMINATOR=r';'
t_ignore=' \t' #space and tabs
t_KEYWORDS=r'BEGIN|END|alias|and|begin|break|case|class|def|defined?|do|else|elsif|end|ensure|false|for|if|in|module|next|nil|not|or|redo|rescue|retry|return|self|super|then|true|unless|until|when|yield|__FILE__|__LINE__|__ENCODING__' 
t_NAME= r'[a-zA-Z_][a-zA-Z0-9_]*'			



#	RegEx with action code
def t_NUMBER(t):
    r'\d+' #docstring representing itd Regex
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'\"[^"]*\"' #docstring representing functions Regex    
    return t


def t_COMMENT(t):
	r'(\=begin(.|\n)*?\=end)|(\#.*)'
	pass



#	Tracking Line no.s
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 	Error handler
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


#	Building the lexer
lexer=lex.lex()
def get_tokens(data):
	'''Returns list of tokens including metadata'''
	lexer.input(data) # using lexer
	tokens=[]
	while(True):
		tok=lexer.token()	
		if not tok:		
			break
		tokens.append((tok.type,tok.value,tok.lineno,tok.lexpos))


	return tokens		


code_file=open('ruby_test.txt','r').read()
#print(code)
tks=get_tokens(code_file)
print(tks)

# Python program to do Lexical Analysis of Ruby code.
import ply.lex as lex
import re
#	Ruby Token List
tokens=('NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN',
	'RPAREN','COMMENT','KEYWORDS','APPEND','STRING','BUILTINMETHOD','RANGE','GREAT','INDENT_T','INDENT_S')

#	RegEx for simple tokens
t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_EQUALS=r'='
t_APPEND=r'<<'
t_RANGE=r'\.\.'
t_ignore=''
t_KEYWORDS=r'BEGIN|END|alias|and|begin|break|case|class|def|defined|do|else|elsif|end|ensure|false|for|if|in|module|next|nil|not|or|redo|rescue|retry|return|self|super|then|true|unless|until|when|yield|__FILE__|__LINE__|__ENCODING__' 
t_NAME= r'[a-zA-Z_][a-zA-Z0-9_]*'			
t_GREAT=r'\>'
t_INDENT_T=r'\t'
t_INDENT_S=r'[ ]'

#	RegEx with action code
def t_NUMBER(t):
    r'\d+' #docstring representing itd Regex
    t.value = int(t.value)    
    return t

def t_BUILTINMETHOD(t):
    r'Array|Float|Integer|String|at_exit|autoload|binding|caller|catch|chop|chop!|chomp|chomp!|eval|exec|exit|exit!|fail|fork|format|gets|global_variables|gsub|gsub!|iterator?|lambda|load|local_variables|loop|open|print|printf|proc|putc|puts|raise|rand|readline|readlines|require|select|sleep|split|sprintf|srand|sub|sub!|syscall|system|test|trace_var|trap|untrace_var' #for built in functions
    return t


def t_STRING(t):
    r'\"[^"]*\"' #docstring representing functions Regex    
    return t

#single line comments
def t_COMMENT(t):
	r'\#[^\n]*'
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
	tokens={}
	while(True):
		tok=lexer.token()	
		if not tok:		
			break
		if(tok.lineno not in tokens.keys()):		
			tokens[tok.lineno]=[]
		tokens[tok.lineno].append((tok.type,tok.value,tok.lineno,tok.lexpos))
	
	d={"BEGIN":'k',"END":'k',"alias":'k',"and":'k',"begin":'k' , "break" :'k',"case":'k',"class":'k',"def":'k',"defined":'k',"do":'k',"else":'k',"elsif":'k',"end":'k',"ensure":'k',"false":'k',"for":'k',"if":'k',"in":'k',"module":'k',"next":'k',"nil":'k',"not":'k',"or":'k',"redo":'k',"rescue":'k',"retry":'k',"return":'k',"self":'k',"super":'k',"then":'k',"true":'k',"unless":'k',"until":'k',"when":'k',"yield":'k',"__FILE__":'k','__LINE__' :'k' ,"__ENCODING__" :'k'}
	ele=0
	block_no=0
	temp={}
	
	for j in tokens.values():
		for k in j:
			if((k[0]=='KEYWORDS') and (k[1] in ['BEGIN','begin','case','class','def','do','else','elsif','for','then','unless','until'])):
				temp={}
				d['block'+str(block_no)]=temp
				block_no+=1
				ele+=1
			if((k[0]=='KEYWORDS') and (k[1] in ['END','end','return','yield'])):
				ele-=1
			if(k[0]=='NAME' and ele!=0):
				temp[k[1]]=0
			elif(k[0]=='NAME'):
				d[k[1]]=0


	print(d)
	return tokens,d		


code_file=open('ruby_test.rb','r').read()
print("\nSymbol Table\n")
tks,symbol_table=get_tokens(code_file)
print("\nTokens\n")
print(tks)

# Python program to do Lexical Analysis of Ruby code.
import ply.lex as lex
import re
#	Ruby Token List
tokens=('while','number','plus','minus','times','divide','equals','lparen','logic','logicnot',
	'rparen','comment','keywords','append','string','builtinmethod','range','great','rsquare','lsquare','newline',
'lflower','rflower','less','begin','break','else','end','for','if','true','false','return','then_tok','elsif','in','do','quotes','dollar','commas','bar','name')

#	RegEx for simple tokens

t_plus=r'\+'
t_minus=r'-'
t_times=r'\*'
t_divide=r'/'
t_lparen=r'\('
t_rparen=r'\)'
t_equals=r'='
t_append=r'<<'
t_range=r'\.\.'
t_ignore='[ \t]'
t_less=r'\<'
#t_if=r'if'
#t_range=r'\.\.\.'

t_keywords=r'alias|case|class|def|defined|ensuremodule|next|nil|redo|rescue|retry|self|super|true|unless|until|when|yield|__FILE__|__LINE__|__ENCODING__' 	
t_lsquare=r'\['
t_rsquare=r'\]'
t_lflower=r'\{'
t_rflower=r'\}'

t_quotes=r'\"'
t_dollar=r'\$'
t_commas=r'\,'
t_bar=r'\|'		
t_great=r'\>'
t_name= r'[a-zA-Z_][a-zA-Z0-9_]*'

#def t_indent_t(t):
#	r'\t'
#	t.lexer.skip(1)
#def t_indent_s(t):
#	r'[ ]'
#	t.lexer.skip(1)


#	RegEx with action code
def t_elsif(t):
	r'elsif'
	return t
def t_while(t):
	r'while'
	return t
def t_begin(t):
	r'begin'
	return t
def t_break(t):
	r'break'
	return t
def t_else(t):
	r'else'
	return t
def t_end(t):
	r'end'
	return t
def t_for(t):
	r'for'
	return t
def t_if(t):
	r'if'
	return t
def t_true(t):
	r'true'
	return t
def t_false(t):
	r'false'
	return t
def t_return(t):
	r'return'
	return t
def t_then_tok(t):
	r'then'
	return t
def t_in(t):
	r'in'
	return t
def t_do(t):
	r'do'
	return t
def t_logic(t):
	r'or|and'
	return t
def t_logicnot(t):
	r'not'
	return t
def t_number(t):
    r'\d+' #docstring representing itd Regex
    t.value = int(t.value)    
    return t

def t_builtinmethod(t):
    r'Array|Float|Integer|String|at_exit|autoload|binding|caller|catch|chop|chop!|chomp|chomp!|eval|exec|exit|exit!|fail|fork|format|gets|global_variables|gsub|gsub!|iterator?|lambda|load|local_variables|loop|open|print|printf|proc|putc|puts|raise|rand|readline|readlines|require|select|sleep|split|sprintf|srand|sub|sub!|syscall|system|test|trace_var|trap|untrace_var' #for built in functions
    return t


def t_string(t):
    r'\"[^"]*\"' #docstring representing functions Regex    
    return t

#single line comments
def t_comment(t):
	r'\#[^\n]*'
	pass

#	Tracking Line no.s
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# 	Error handler
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


#	Building the lexer
lexer=lex.lex()
def get_tokens(data):
	#Returns list of tokens including metadata
	lexer.input(data) # using lexer
	tokens={}
	#symbol_table={}
	while(True):
		tok=lexer.token()	
		if not tok:		
			break
		if(tok.lineno not in tokens.keys()):		
			tokens[tok.lineno]=[]
		tokens[tok.lineno].append((tok.type,tok.value,tok.lineno,tok.lexpos))
	
	d={"BEGIN":'k',"END":'k',"alias":'k',"and":'k',"begin":'k' , "break" :'k',"case":'k',"class":'k',"def":'k',"defined":'k',"do":'k',"else":'k',"elsif":'k',"end":'k',"ensure":'k',"false":'k',"for":'k',"if":'k',"in":'k',"module":'k',"next":'k',"nil":'k',"not":'k',"or":'k',"redo":'k',"rescue":'k',"retry":'k',"return":'k',"self":'k',"super":'k',"then":'k',"true":'k',"unless":'k',"until":'k',"when":'k',"yield":'k',"__FILE__":'k','__LINE__' :'k' ,"__ENCODING__" :'k',-1:1}
	#d={-1:1}	
	for j in tokens.values():
		for k in j:
			if 'name' in k[0]:
				d[k[1]]=None	

	#print(d)
	#print(symbol_table)
	return tokens,d		


code_file=open('ruby_test.rb','r').read()
#print("\nSymbol Table\n")
tks,symbol_table=get_tokens(code_file)
#print("\nTokens\n")
#print(tks)
#sprint("Symbol Table\n")


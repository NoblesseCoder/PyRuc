import ply.lex as lex
import re
import string 
import random
from ST import SymbolTable


class LA(object):
	'''Tokenize input steam'''

	# List of token names
	tokens=('while','number','plus','minus','times','divide','equals','lparen',
		'logic','logicnot','rparen','comment','keywords','append','string','builtinmethod',
		'range','great','rsquare','lsquare','newline','lflower','rflower','less','begin','break',
		'else','end','for','if','true','false','return','then_tok','elsif','in','do',
		'quotes','dollar','commas','bar','name')

	# Regex rules for simple Tokens
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
	t_keywords=r'true|unless|until|when' 	
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

	# Regex rules with action code

	def t_elsif(self,t):
		r'elsif'
		return t

	def t_while(self,t):
		r'while'
		return t
	
	def t_begin(self,t):
		r'begin'
		return t
	
	def t_break(self,t):
		r'break'
		return t
	
	def t_else(self,t):
		r'else'
		return t
	
	def t_end(self,t):
		r'end'
		return t
	
	def t_for(self,t):
		r'for'
		return t
	
	def t_if(self,t):
		r'if'
		return t
	
	def t_true(self,t):
		r'true'
		return t
	
	def t_false(self,t):
		r'false'
		return t
	
	def t_return(self,t):
		r'return'
		return t
	
	def t_then_tok(self,t):
		r'then'
		return t
	
	def t_in(self,t):
		r'in'
		return t
	
	def t_do(self,t):
		r'do'
		return t
	
	def t_logic(self,t):
		r'or|and'
		return t
	
	def t_logicnot(self,t):
		r'not'
		return t
	
	def t_number(self,t):
	    r'\d+' #docstring representing itd Regex
	    t.value = int(t.value)    
	    return t

	def t_builtinmethod(self,t):
	    r'Array|Float|Integer|String|at_exit|autoload|binding|caller|catch|chop|chop!|chomp|chomp!|eval|exec|exit|exit!|fail|fork|format|gets|global_variables|gsub|gsub!|iterator?|lambda|load|local_variables|loop|open|print|printf|proc|putc|puts|raise|rand|readline|readlines|require|select|sleep|split|sprintf|srand|sub|sub!|syscall|system|test|trace_var|trap|untrace_var' #for built in functions
	    return t


	def t_string(self,t):
	    r'\"[^"]*\"' #docstring representing functions Regex    
	    return t


	#Handling single line comments
	def t_comment(self,t):
		r'\#[^\n]*'
		pass

	#Tracking Line no.s
	def t_newline(self,t):
	    r'\n+'
	    t.lexer.lineno += len(t.value)
	    return t

	#Error handler 	
	def t_error(self,t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	#Building The Lexer
	def build(self,**kwargs):
		self.lexer=lex.lex(module=self,**kwargs)

	#Generating tokens	
	def tokenize(self,data):
		tkns=[]
		self.lexer.input(data)
		while(True):
			tok=self.lexer.token()
			if not tok:
				break
			if(tok.type != 'newline'):		
				tkns.append([tok.type,tok.value])
		return(tkns)	
				

# Testing
code_file=open('test.rb','r').read()
l=LA()
l.build()
tks=l.tokenize(code_file)
st=SymbolTable()
symbol_table=st.gen_st(tks)

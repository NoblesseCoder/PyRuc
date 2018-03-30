# Python program to do Lexical Analysis of Ruby code.
# We are not taking into consideration strings in single quotes here , gives an error with single quotes
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
	

	#remove the tuples with spaces and tabs
	for i in range(0,len(tokens)):
		list1 = []
		keys = list(tokens.keys())
		required_key = int(keys[i])
		for j in range(0,len(tokens[required_key])):
			if(tokens[required_key][j][0] != 'INDENT_T' and  tokens[required_key][j][0] != 'INDENT_S'):
				list1.append(tokens[required_key][j])
		tokens[required_key] = list1

	#add datatype to the variables
	d = {}
	scope_no = 0
	for j in tokens.values():
		length = len(j)
		for k in range(0,length):
			if((j[k][0]=='KEYWORDS') and (j[k][1] in ['BEGIN','begin','case','class','def','do','else','elsif','for','unless','until','if'])):			
				scope_no = scope_no + 1	
			if((j[k][0]=='KEYWORDS') and (j[k][1] in ['END','end','return','yield'])):
				scope_no = scope_no - 1
			if(j[k][0] == 'BUILTINMETHOD'):
				list1 = []
				list1.append('predefined') #represents the type
				 #represents the scope , where 0 represents global varaibles
				d[j[k][1]] = list1
			if(j[k][0] == 'NAME'):
				list1 = []
				l = k+1	
				m = k+2			
				if(j[l][0] == 'EQUALS'):
					if('.' in str(j[m][1])):
						list1.append('float')
					else:
						list1.append('integer')
				else:
					list1.append('iterable')
				list1.append(scope_no)
				if(j[k][1] not in d.keys()):
					d[j[k][1]] = list1

			if(j[k][0] == 'NAME' and j[k+1][0] == 'EQUALS' and j[k+2][0]== 'STRING'):
				list1 = []
				l= k+1
				m = k+2
				list1.append('string')
				list1.append(scope_no)
				d[j[k][1]] = list1

			
			
				
		
	#print(d)
	print(tokens)
	return tokens,d		


code_file=open('ip.rb','r').read()
print("\nSymbol Table\n")
tks,symbol_table=get_tokens(code_file)
print("\nSymbol Table with Scope no and data type of varaibles and predefined functions\n")
for k, v in symbol_table.items():
	print(k, v)



import ply.yacc as yacc
import logging
from lexer import LA
from lexer import symbol_table
import lexer
tokens=LA.tokens

#Precedence rules for parsing
precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'times', 'divide'),
)

#Grammar for language(Assignment,Selection & loop)

end_label=[]
queue=[]
queue_cond=[]
queue_labels=[]
temp_counter=0
label_counter=0
def p_PROGRAM(p):
	'''PROGRAM : BLOCKSTMT
	'''
	r=open('icg.txt','w')
	r.write(p[1])
def p_BLOCKSTMT(p): 
	'''BLOCKSTMT : T STMT T BLOCKSTMT	
	| T STMT T 
	'''
	if(len(p)==5):
		if(p[2] is None):
			p[2]=''
		if(p[4] is None):
			p[4]=''		
		p[0]=p[2] + '\n' + p[4]

	elif(len(p)==4):
		if(p[2] is None):
			p[2]=''
		if('\n' in p[2]):
			p[0]=p[2]
		else:
			p[0]=p[2]

def p_T(p):
	'''T : T newline
	|
	'''
def p_STMT(p):
	'''STMT : ASSGN
	| SELECT
	| ITER
	'''
	p[0]=p[1]

def p_SELECT(p):
	'''SELECT : if CONDEXPR EMPTQC then_tok T BLOCKSTMT LABELMAKER LABEL_E ELSIF ELSE end 
	'''
	global end_label
	a=end_label.pop()
	p[0] = p[3]+'ifFalse ' + str(p[2]) +' '+ 'goto' + ' ' +p[7][:-1] +'\n'+ str(p[6])+'\n'+'goto '+ a + '\n'+ str(p[7]) + str(p[9])+ '\n' + str(p[10])+'\n' + a + ':'	
	
def p_LABEL_E(p):
	'''LABEL_E :'''
	global label_counter
	end_label.append('L'+str(label_counter))
	label_counter+=1

def p_EMPTQC(p):
	'''EMPTQC :'''
	temp2=''
	flag=False	
	if(len(queue_cond)!=0):
		a=queue_cond.pop(0)
		flag=True
	while(len(queue_cond)!=0):
		temp2+=a+'\n'
		a=queue_cond.pop(0)
	if(flag):
		temp2+=a
	p[0]=temp2


def p_LABELMAKER(p):
	'''LABELMAKER :'''
	global label_counter
	p[0]="L" + str(label_counter)+':'
	label_counter+=1

def p_ELSIF(p):
	'''ELSIF : elsif CONDEXPR then_tok T BLOCKSTMT LABELMAKER
	|
	'''
	if len(p)==1 :
		p[0]=''
	else:
		#p[0]= str(p[2])
		temp2=''
		flag=False	
		if(len(queue_cond)!=0):
			a=queue_cond.pop(0)
			flag=True
		while(len(queue_cond)!=0):
			temp2+=a+'\n'
			a=queue_cond.pop(0)
		if(flag):
			temp2+=a
		p[0]= temp2+'ifFalse ' + str(p[2])+' goto '+str(p[6][:-1]) + '\n' + str(p[5]) +'\n' + 'goto '+ end_label[-1] +'\n' +str(p[6])

def p_ELSE(p):
	'''ELSE : else BLOCKSTMT
	|
	'''
	if len(p)==1 :
		p[0]=''
	else:
		p[0]= str(p[2])
			
	
def p_CONDEXPR(p):
	'''CONDEXPR : EXPR less EXPR
	| EXPR equals equals EXPR
	| EXPR great EXPR
	| EXPR great equals EXPR
	| EXPR less equals EXPR
	'''	
	if(len(p)==4):
		flag=False
		if(len(queue)!=0):
			a=queue.pop(0)
			flag=True
		while(len(queue)!=0):
			queue_cond.append(a)
			a=queue.pop(0)
		if(flag):
			queue_cond.append(a)
		#print(p[1],"hello")
		if(('=' in str(p[1])) or ('=' in str(p[3]))):
			temp1=''
			#print(p[1],"hello")
			if('=' in str(p[1])):
				i=''	
				for i in str(p[1]):
					if '=' not in i:
						temp1+=i
					else:
						break
				queue_cond.append(p[1])				
				p[1]=temp1
				#print(p[1],"hello")
			temp2=''
			if('=' in str(p[3])):
				i=''
				for i in str(p[3]):
					if '=' not in i:
						temp2+=i
					else:
						break
				queue_cond.append(p[3])				
				p[3]=temp2	
				#print(p[1],p[3])
		p[0] = str(p[1]) + ' ' + str(p[2]) + ' ' + str(p[3])

	else:
		flag=False
		if(len(queue)!=0):
			a=queue.pop(0)
			flag=True
		while(len(queue)!=0):
			queue_cond.append(a)
			a=queue.pop(0)
		if(flag):
			queue_cond.append(a)
	#print(p[1],"hello")
		if(('=' in str(p[1])) or ('=' in str(p[3]))):
			temp1=''
		#print(p[1],"hello")
			if('=' in str(p[1])):
				i=''	
				for i in str(p[1]):
					if '=' not in i:
						temp1+=i
					else:
						break
				queue_cond.append(p[1])				
				p[1]=temp1
				#print(p[1],"hello")
			temp2=''
			if('=' in str(p[4])):
				i=''
				for i in str(p[4]):
					if '=' not in i:
						temp2+=i
					else:
						break
				queue_cond.append(p[4])				
				p[4]=temp2	
			#print(p[1],p[3])
		p[0] = str(p[1]) + ' ' + str(p[2]) + str(p[3]) + ' ' + str(p[4])	
		

def p_ASSGN(p):
	'''ASSGN : LHS equals EXPR
	'''
	temp1=''
	temp2=''
	#print(p[1],"hello")
	if('=' in str(p[3])):
		i=''	
		for i in str(p[3]):
			if '=' not in i:
				temp1+=i
			else:
				break
		#print(p[3])
		queue.append(p[3])				
		p[3]=temp1
			#print(p[1],"hello")	
		a=queue.pop(0)		
		while(len(queue)!=0):
			temp2+=a +'\n'
			a=queue.pop(0)
		temp2+=a
	try:
		a=int(p[3])
		symbol_table[p[1]]=a
		#print('symbol table updated')
		#print(symbol_table)
	except:
		symbol_table[str(p[1])]='defined'
	p[0]=temp2 + str(p[1]) + ' ' + str(p[2]) + ' ' + str(p[3])

def p_LHS(p):
	'''LHS : name
	'''
	p[0]=p[1]
	#print(p[1])
def p_EXPR(p):
	'''EXPR : EXPR plus EXPR
	| EXPR minus EXPR
	| EXPR times EXPR
	| EXPR divide EXPR
	| name
	| number
	'''
	if(len(p)==4):
		global temp_counter
		if(('=' in str(p[1])) or ('=' in str(p[3]))):
			temp1=''
			#print(p[1],"hello")
			if('=' in str(p[1])):
				i=''	
				for i in str(p[1]):
					if '=' not in i:
						temp1+=i
					else:
						break
				queue.append(p[1])				
				p[1]=temp1
			#print(p[1],"hello")
			temp2=''
			if('=' in str(p[3])):
				i=''
				for i in str(p[3]):
					if '=' not in i:
						temp2+=i
					else:
						break
				queue.append(p[3])				
				p[3]=temp2	
			#print(p[1],p[3])
		p[0]='t'+str(temp_counter)+' = '+str(p[1])+' '+str(p[2])+' '+str(p[3]) + '\n'
		temp_counter+=1
	elif(len(p)==2): #check in symbol table here
		try:
			int(p[1])
		except ValueError:
			if(symbol_table[p[1]]==None):
				raise ValueError("Variable "+ str(p[1])+ ' has not been defined')
		p[0]=p[1]
	

		
        #check for nos here


def p_ITER(p):
	'''ITER : while LABELMAKER CONDEXPR EMPTQC do T BLOCKSTMT T end LABELMAKER
	'''
	p[0]= str(p[2]) + str(p[4]) + '\n' +'ifFalse ' + p[3] + ' goto ' + p[10][:-1] + '\n' + p[7] + '\n' + 'goto ' + str(p[2][:-1]) + '\n' + p[10]   
	
	

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()




# Build the parser
parser = yacc.yacc()

s = open('test.rb','r').read()

result = parser.parse(s,debug=log)
#print(log)
if result is not None:
	with open("AST.txt",'w') as f:
		f.write(str(result))




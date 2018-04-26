import random
import string

class SymbolTable:
	'''Symbol Table for the compiler'''
	
	def __init__(self,size=3):
		self.size=size
		self.st={}

	def id_gen(self):
		'''Random id generation for symbol table enteries '''
		
		chars=string.ascii_lowercase + string.digits
		return(''.join(random.choice(chars) for _ in range(self.size)))		

	def gen_st(self,tokens):
		'''Initialize symbol table with keywords & tokens'''

		st={"BEGIN":'k_'+self.id_gen(),"END":'k_'+self.id_gen(),"and":'k_'+self.id_gen(),"begin":'k_'+self.id_gen(),
		"break" :'k_'+self.id_gen(),"do":'k_'+self.id_gen(),"else":'k_'+self.id_gen(),"elsif":'k_'+self.id_gen(),
		"end":'k_'+self.id_gen(),"false":'k_'+self.id_gen(),"for":'k_'+self.id_gen(),"if":'k_'+self.id_gen(),
		"in":'k_'+self.id_gen(),"not":'k_'+self.id_gen(),"or":'k_'+self.id_gen(),"redo":'k_'+self.id_gen(),
		"return":'k_'+self.id_gen(),"self":'k_'+self.id_gen(),"then":'k_'+self.id_gen(),"true":'k_'+self.id_gen(),
		"unless":'k_'+self.id_gen(),"until":'k_'+self.id_gen(),"when":'k_'+self.id_gen(),"yield":'k_'+self.id_gen()}

		for tok in tokens:
			self.st[tok[1]]=None
		
		return(self.st)	


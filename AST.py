debugNode = False


class Node(object):
	def printast(self):
		return "NOT IMPLEMENTED!"

	def insertLineNumInfo(self, linenumber, position):
		self.line_position = (linenumber, position)

	def position(self):
		return "Line %d, Column %d" % self.line_position

class BlockStmt(Node):
	def __init__(self,stmt=None,Blockstmt = None):
		self.Stmt = stmt
		self.BlockStmt = Blockstmt

	def __str__(self):
		outputstr = "[BlockStmt] :\n"
		if self.Stmt is not None:
			outputstr += "Stmt : " + str(self.Stmt)
		if self.BlockStmt is not None:
			outputstr +=  "Blockstmt : " + str(self.BlockStmt)	
		return outputstr
	
	def printast(self):
		outputstr = ""
		if debugNode:
			outputstr += "[BlockStmt]"
		if self.Stmt is not None:
			outputstr += self.Stmt.printast()
			outputstr += "\n"
		if self.BlockStmt is not None:
			outputstr += self.BlockStmt.printast()
		return outputstr

		
class Identifier(Node):
	def __init__(self, id, idtype="non-array"):
		self.Identifier = id
		self.idtype = idtype                # This value is either 'array' or 'non-array'

	def __str__(self):
		outputstr = "[Identifier] : \n"
		if self.Identifier is not None:
			outputstr += "id : " + str(self.Identifier) + ","
		if self.idtype is not None:
			outputstr += "idtype : " + str(self.idtype)
		return outputstr

	def printast(self):
		return str(self.Identifier)


class WhileStmt(Node):
	def __init__(self, style, conditionexpr, repeatstmt):
		self.style = style                  # This value is either 'while'
		self.Expr = conditionexpr
		self.BlockStmt = repeatstmt

	def __str__(self):
		outputstr = "[WhileStmt] : \n"
		if self.style is not None:
			outputstr += "style : " + str(self.style)
		if self.Expr is not None:
			outputstr += "conditionexpr : " + str(self.Expr)
		if self.BlockStmt is not None:
			outputstr += "blockstmt : " + str(self.BlockStmt)
		return outputstr

	def printast(self):
		outputstr = ""
		if self.style == "while":
			outputstr += "while "
			outputstr += self.Expr.printast()
			outputstr += "do "
			outputstr += self.BlockStmt.printast()
			outputstr += "end"

		return outputstr

class Expr(Node):
	def __init__(self, expr_type, operand1=None, operand2=None, operator=None, idval=None, idIDX=None):
		self.expr_type = expr_type
        # This expr_type value is either
        # 'unop', 'binop'
        # 'call', 'intnum', 'floatnum', 'id', 'arrayID'
		self.operator = operator
        # This value can be 'unop',  PLUS, MINUS, TIMES, DIVIDE, ...
		self.operand1 = operand1
		self.operand2 = operand2

	def __str__(self):
		outputstr = "[Expr] : \n"
		if self.expr_type is not None:
			outputstr += "expr_type : " + str(self.expr_type)
		if self.operator is not None:
			outputstr += "operator : " + str(self.operator)
		if self.operand1 is not None:
			outputstr += "operand1 : " + str(self.operand1)
		if self.operand2 is not None:
			outputstr += "operand2 : " + str(self.operand2)
		return outputstr

	def printast(self):
		if self.expr_type == "binop":
			return self.operand1.printast()+str(self.operator)+self.operand2.printast()
		elif self.expr_type == "id":
			return str(self.operand1)
		else:  # intnum/floatnum case
			return str(self.operand1)

   

class IfStmt(Node):
	def __init__(self, conditionexpr, thenstmt, elseifstmt,elsestmt =None):
		self.Expr = conditionexpr
		self.BlockStmt = thenstmt
		self.elseif = elseifstmt
		self.elsestmt = elsestmt

	def __str__(self):
		outputstr = "[ifStmt] : \n"
		if self.Expr is not None:
			outputstr += "conditionexpr : " + str(self.Expr)
		if self.BlockStmt is not None:
			outputstr += "thenstmt : " + str(self.BlockStmt)
		if self.elseif is not None:
			outputstr += "elseif: " + str(self.elseif)
		if self.elsestmt is not None:
			outputstr += "elsestmt : " + str(self.elsestmt)
		return outputstr

	def printast(self):
		outputstr = "if "
		outputstr += self.Expr.printast() + "then \n"
		outputstr += self.BlockStmt.printast() + "\n"
		if self.elseif is not None:
			outputstr += "elseif\n" + self.elseif.printast()
		if self.elsestmt is not None:
			outputstr += "else\n" + self.elsestmt.printast()
		outputstr += "end\n"
		return outputstr


class Stmt(Node):
	def __init__(self, stmttype, stmt):
		self.stmttype = stmttype
		self.Stmt = stmt
	
	def printast(self):
		outputstr = ""
		outputstr += self.Stmt.printast()
		return outputstr


class Assign(Node):
	def __init__(self, assigntype, id, expr):
		self.assigntype = assigntype        # This value is either 'array' or 'non-array'
		self.Identifier = id
		self.Expr = expr
		
	def __str__(self):
		outputstr = "[Assign] : \n"
		if self.assigntype is not None:
			outputstr += "assigntype : " + str(self.assigntype)
		if self.Identifier is not None:
			outputstr += "id : " + str(self.Identifier)
		if self.Expr is not None:
			outputstr += "Expr: " + str(self.Expr)
		return outputstr

	def printast(self):
		if self.assigntype == "non-array":
			return str(self.Identifier)+" = "+self.Expr.printast()
      

class elsestmt(Node):
	def __init__(self, blockstmt):
		self.BlockStmt = blockstmt

	def __str__(self):
		outputstr = "[else] : \n"
		if self.BlockStmt is not None:
			outputstr += "Blockstmt : " + str(self.BlockStmt)
		return outputstr

	def printast(self):
		outputstr = "else "
		outputstr += self.BlockStmt.printast() +  "\n"
		return outputstr


def elseif(Node):
	def __init__(self,expr,blockstmt):
		self.Expr = expr
		self.BlockStmt = blockstmt
	
	def __str__(self):
		outputstr = "[elseif] : \n"
		if self.Expr is not None:
			outputstr += "Expr : " + str(self.Expr)
		if self.BlockStmt is not None:
			outputstr += "Blockstmt : " + str(self.BlockStmt)
		return outputstr

	def printast(self):
		outputstr = "elseif "
		outputstr += self.Expr.printast() + "\n"
		outputstr += "then \n"
		outputstr += self.BlockStmt.printast()
		return outputstr


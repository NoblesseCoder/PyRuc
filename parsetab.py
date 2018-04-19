
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftplusminuslefttimesdividewhile number plus minus times divide equals lparen logic logicnot rparen comment keywords append string builtinmethod range great rsquare lsquare newline lflower rflower less begin break else end for if true false return then_tok elsif in do quotes dollar commas bar nameBLOCKSTMT : STMT newline BLOCKSTMT\n\t| STMT BLOCKSTMT\t\n\t| STMT newline\n\t| STMT\n\tSTMT : ASSGN\n\t| SELECT\n\t| ITER\n\tSELECT : if EXPR then_tok BLOCKSTMT ELSIF ELSE end\n\tELSIF : elsif EXPR then_tok BLOCKSTMT\n\t|\n\tELSE : else BLOCKSTMT\n\t|\n\tASSGN : LHS equals EXPR\n\tLHS : name\n\tEXPR : EXPR plus EXPR\n\t| EXPR minus EXPR\n\t| EXPR times EXPR\n\t| EXPR divide EXPR\n\t| EXPR less EXPR\n\t| EXPR equals equals EXPR\n\t| EXPR great EXPR\n\t| EXPR great equals EXPR\n\t| EXPR less equals EXPR\n\t| name\n\t| number\n\tITER : while EXPR do BLOCKSTMT end\n\t'
    
_lr_action_items = {'if':([0,2,3,4,5,10,14,15,18,19,27,29,30,31,32,33,36,41,42,43,44,46,48,50,],[7,7,-5,-6,-7,7,-24,-25,-13,7,7,-15,-16,-17,-18,-19,-21,-23,-20,-22,-26,7,-8,7,]),'while':([0,2,3,4,5,10,14,15,18,19,27,29,30,31,32,33,36,41,42,43,44,46,48,50,],[8,8,-5,-6,-7,8,-24,-25,-13,8,8,-15,-16,-17,-18,-19,-21,-23,-20,-22,-26,8,-8,8,]),'name':([0,2,3,4,5,7,8,10,12,14,15,18,19,20,21,22,23,24,26,27,29,30,31,32,33,34,35,36,37,40,41,42,43,44,46,48,50,],[9,9,-5,-6,-7,14,14,9,14,-24,-25,-13,9,14,14,14,14,14,14,9,-15,-16,-17,-18,-19,14,14,-21,14,14,-23,-20,-22,-26,9,-8,9,]),'$end':([1,2,3,4,5,10,11,14,15,17,18,29,30,31,32,33,36,41,42,43,44,48,],[0,-4,-5,-6,-7,-3,-2,-24,-25,-1,-13,-15,-16,-17,-18,-19,-21,-23,-20,-22,-26,-8,]),'newline':([2,3,4,5,14,15,18,29,30,31,32,33,36,41,42,43,44,48,],[10,-5,-6,-7,-24,-25,-13,-15,-16,-17,-18,-19,-21,-23,-20,-22,-26,-8,]),'elsif':([2,3,4,5,10,11,14,15,17,18,28,29,30,31,32,33,36,41,42,43,44,48,],[-4,-5,-6,-7,-3,-2,-24,-25,-1,-13,40,-15,-16,-17,-18,-19,-21,-23,-20,-22,-26,-8,]),'else':([2,3,4,5,10,11,14,15,17,18,28,29,30,31,32,33,36,39,41,42,43,44,48,51,],[-4,-5,-6,-7,-3,-2,-24,-25,-1,-13,-10,-15,-16,-17,-18,-19,-21,46,-23,-20,-22,-26,-8,-9,]),'end':([2,3,4,5,10,11,14,15,17,18,28,29,30,31,32,33,36,38,39,41,42,43,44,45,48,49,51,],[-4,-5,-6,-7,-3,-2,-24,-25,-1,-13,-10,-15,-16,-17,-18,-19,-21,44,-12,-23,-20,-22,-26,48,-8,-11,-9,]),'equals':([6,9,13,14,15,16,18,24,25,26,29,30,31,32,33,36,41,42,43,47,],[12,-14,25,-24,-25,25,25,34,35,37,-15,-16,-17,-18,25,25,25,25,25,25,]),'number':([7,8,12,20,21,22,23,24,26,34,35,37,40,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'then_tok':([13,14,15,29,30,31,32,33,36,41,42,43,47,],[19,-24,-25,-15,-16,-17,-18,-19,-21,-23,-20,-22,50,]),'plus':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[20,-24,-25,20,20,-15,-16,-17,-18,20,20,20,20,20,20,]),'minus':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[21,-24,-25,21,21,-15,-16,-17,-18,21,21,21,21,21,21,]),'times':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[22,-24,-25,22,22,22,22,-17,-18,22,22,22,22,22,22,]),'divide':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[23,-24,-25,23,23,23,23,-17,-18,23,23,23,23,23,23,]),'less':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[24,-24,-25,24,24,-15,-16,-17,-18,24,24,24,24,24,24,]),'great':([13,14,15,16,18,29,30,31,32,33,36,41,42,43,47,],[26,-24,-25,26,26,-15,-16,-17,-18,26,26,26,26,26,26,]),'do':([14,15,16,29,30,31,32,33,36,41,42,43,],[-24,-25,27,-15,-16,-17,-18,-19,-21,-23,-20,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'BLOCKSTMT':([0,2,10,19,27,46,50,],[1,11,17,28,38,49,51,]),'STMT':([0,2,10,19,27,46,50,],[2,2,2,2,2,2,2,]),'ASSGN':([0,2,10,19,27,46,50,],[3,3,3,3,3,3,3,]),'SELECT':([0,2,10,19,27,46,50,],[4,4,4,4,4,4,4,]),'ITER':([0,2,10,19,27,46,50,],[5,5,5,5,5,5,5,]),'LHS':([0,2,10,19,27,46,50,],[6,6,6,6,6,6,6,]),'EXPR':([7,8,12,20,21,22,23,24,26,34,35,37,40,],[13,16,18,29,30,31,32,33,36,41,42,43,47,]),'ELSIF':([28,],[39,]),'ELSE':([39,],[45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> BLOCKSTMT","S'",1,None,None,None),
  ('BLOCKSTMT -> STMT newline BLOCKSTMT','BLOCKSTMT',3,'p_BLOCKSTMT','yacc.py',10),
  ('BLOCKSTMT -> STMT BLOCKSTMT','BLOCKSTMT',2,'p_BLOCKSTMT','yacc.py',11),
  ('BLOCKSTMT -> STMT newline','BLOCKSTMT',2,'p_BLOCKSTMT','yacc.py',12),
  ('BLOCKSTMT -> STMT','BLOCKSTMT',1,'p_BLOCKSTMT','yacc.py',13),
  ('STMT -> ASSGN','STMT',1,'p_STMT','yacc.py',16),
  ('STMT -> SELECT','STMT',1,'p_STMT','yacc.py',17),
  ('STMT -> ITER','STMT',1,'p_STMT','yacc.py',18),
  ('SELECT -> if EXPR then_tok BLOCKSTMT ELSIF ELSE end','SELECT',7,'p_SELECT','yacc.py',21),
  ('ELSIF -> elsif EXPR then_tok BLOCKSTMT','ELSIF',4,'p_ELSIF','yacc.py',25),
  ('ELSIF -> <empty>','ELSIF',0,'p_ELSIF','yacc.py',26),
  ('ELSE -> else BLOCKSTMT','ELSE',2,'p_ELSE','yacc.py',29),
  ('ELSE -> <empty>','ELSE',0,'p_ELSE','yacc.py',30),
  ('ASSGN -> LHS equals EXPR','ASSGN',3,'p_ASSGN','yacc.py',33),
  ('LHS -> name','LHS',1,'p_LHS','yacc.py',37),
  ('EXPR -> EXPR plus EXPR','EXPR',3,'p_EXPR','yacc.py',41),
  ('EXPR -> EXPR minus EXPR','EXPR',3,'p_EXPR','yacc.py',42),
  ('EXPR -> EXPR times EXPR','EXPR',3,'p_EXPR','yacc.py',43),
  ('EXPR -> EXPR divide EXPR','EXPR',3,'p_EXPR','yacc.py',44),
  ('EXPR -> EXPR less EXPR','EXPR',3,'p_EXPR','yacc.py',45),
  ('EXPR -> EXPR equals equals EXPR','EXPR',4,'p_EXPR','yacc.py',46),
  ('EXPR -> EXPR great EXPR','EXPR',3,'p_EXPR','yacc.py',47),
  ('EXPR -> EXPR great equals EXPR','EXPR',4,'p_EXPR','yacc.py',48),
  ('EXPR -> EXPR less equals EXPR','EXPR',4,'p_EXPR','yacc.py',49),
  ('EXPR -> name','EXPR',1,'p_EXPR','yacc.py',50),
  ('EXPR -> number','EXPR',1,'p_EXPR','yacc.py',51),
  ('ITER -> while EXPR do BLOCKSTMT end','ITER',5,'p_ITER','yacc.py',54),
]
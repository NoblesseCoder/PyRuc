# PyRuc-(Python based Ruby Compiler)

We Implemented this as a part of the Complier Design Lab Course at PES University.The following Details are taken from PESU's Compiler Lab Mini Project Guidelines.

This repo contains an implementation of a Compiler for Ruby written in Python by making use of the ***PLY (i.e Pythonic Version of Lex & Yacc Tools) package***. A thing to note is that this is just a Front End Compiler i.e it doesn't implement the Machine Dependent Code optimization (MDCO) Phase out of the seven standard phases of Compilation. Also it is implemented to compile a few basic constructs of Ruby only & can be extended to include more. 

## The Phases it Implements:

### 1. Lexical Analysis Phase & Symbol Table Construction:

1.  Remove Comments.
2.  Generate tokens.
3.  Preload keywords into the Symbol Table.
4.  Make an entry for the identifiers into the Symbol Table (if there exists an identifier with the same name in different scopes then construct Symbol Table per scope)
5.  Symbol Table must contain entries for predefined routines like printf, scanf etc.

### 2. Syntax Analysis Phase:

6.  Write CFG for the entire program using appropriate Semantic rules if you are using PLY.
7.  Else if you are implementing Parser by hand use Recursive Descent Parser (RDP) with Backtracking & Perform translation at required places in the code for each non-terminal.

### 3. Semantic Analysis Phase (In this Project we look at basic Semantic Constructs only):

8.  Take care of the primitive types and array types.
9.  Take care of coersions.
10. Take care of Arithemetic Expressions.
11. Concetrate on the looping construct choosen.
12. Update type and storage information into the symbol table.
13. Show Abstract Syntax tree (AST).

### 4. Intermediate Code Generation:

14. Do a Three address code generation.

### 5. Machine Independent Code Optimization (MDCO):

15. Perform Constant folding.
16. Perform Constant Propogation.
17. Perform Common subexpression elimination.
18. Perform Dead code elimination.

These are some of the basic optimizations that are implemented in this Project.You can extend the same to add more optimizations like Reducing temporaries, Loop optimizations etc.


The remaining 2 phases that form the Backend of the Compiler are Machine Dependent Code Generation (MDCO) & Target Code Generation which are not implmented here.

Link to the PLY Package: https://www.dabeaz.com/ply/ply.html

To Understand more about the Compier's phases you can checkout the ***Compliers: Principles, Techniques & Tools*** Book (more famously known as the Dragon Book) by Aho et al.
Link- https://www.amazon.in/Compilers-Alfred-V-Aho/dp/9332542457?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_CjwKCAjwstfkBRBoEiwADTmnEHm7nMy2Ma_kjQqmHPMuiqdM2SX5V8V11nI4GnC7hVKgrKfsH4yOnxoCJzoQAvD_BwE_k_&gclid=CjwKCAjwstfkBRBoEiwADTmnEHm7nMy2Ma_kjQqmHPMuiqdM2SX5V8V11nI4GnC7hVKgrKfsH4yOnxoCJzoQAvD_BwE 
 

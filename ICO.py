import ast
import copy
filein=open('icg.txt','r')
fileout=open('oic.txt','w')
a=filein.readlines()
update_table={}
result=''
b=[i for i in a if i!='\n']
for i in b:
	if '=' in i and '<' not in i and '>' not in i and '==' not in i: #only assignment
		k=copy.deepcopy(i)	
		k=k.split('=')
		try:
			k[0]=k[0].replace(" ",'')
			a=int(k[1])
			if k[0] in update_table.keys():
				update_table[k[0]]=a
			else:
				update_table[k[0]]=a
		except:
			update_table[k[0]]=None			
			temp=copy.deepcopy(i)
			temp=temp.split(' ')
			for j in update_table.keys():
				for k in range(len(temp)):
					if j == temp[k] and update_table[j]!=None:
						temp[k]=update_table[j]
			for j in temp:
				if j != '\n':
					result+=str(j) + ' '
				else:
					result+='\n'
					break
	else:
		temp=copy.deepcopy(i)
		temp=temp.split(' ')
		for j in update_table.keys():
			for k in range(len(temp)):
				if j == temp[k] and update_table[j]!=None:
					temp[k]=update_table[j]
		for j in temp:
			if j != '\n':
				result+=str(j) + ' '
			else:
				result+='\n'
				break
	#result+=i
import io
result=io.StringIO(result)
b=result.readlines()
result=''
for i in b:
	if '=' in i and '<' not in i and '>' not in i and '==' not in i: #only assignment
		k=copy.deepcopy(i)	
		k=k.split('=')
		try:
			k[1]=k[1].replace(" ",'')
			#print(k[1])
			k[1]=ast.literal_eval(k[1])
			k=k[0] + ' = ' + str(k[1])
		except:
			k=k[0] + ' = ' + k[1]
		result+=k+'\n'
	else:
		result+=i		
			
#print(b)
fileout.write(result)		
#print(b)


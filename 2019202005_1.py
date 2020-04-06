import sys

f=open('input.txt','r')
l=f.readlines()
f.close()

x=3
t_count=0
data=[]
res=[]
var=l[0].strip()
log=[]

vardict={}			#Variables present in disk
inmemvardict={}		#variables present in memory
tempvardict={}		#Temp variables present

tot=0
lengths={}
transdict={}
indexes=[0]*x

def printme():
	temp=""
	for i in sorted(inmemvardict):
		temp=temp+i+" "+str(inmemvardict[i])+" "
	log.append(temp)

	temp=""
	for i in sorted(vardict):
		temp=temp+i+" "+str(vardict[i])+" "
	log.append(temp)

def do_ops(transaction,t):
	# print('do ops')
	
	if("READ" in t):
		print(transaction,t)
		i,j =(t.split("(")[1]).split(",")
		j=j.strip(')')

		print(i,j)

		if(i in inmemvardict.keys()):
			print(i, 'is present in memory')
			tempvardict[j]=inmemvardict[i]
		else:
			print(i,' needs to be loaded from disk')
			inmemvardict[i]=int(vardict[i])
			tempvardict[j]=int(vardict[i])


	if("WRITE" in t):
		print(transaction,t)

		i,j =(t.split("(")[1]).split(",")
		j=j.strip(')')

		print(i,j)
		oldval=inmemvardict[i]
		log.append("<"+transaction+", "+str(i)+", "+str(oldval)+">")
		newval=tempvardict[j]
		inmemvardict[i]=newval
		printme()

	if("OUTPUT" in t):

		# i,j =(t.split("(")[1]).split(",")
		# j=j.strip(')')

		pass

	if("+" in t):
		print('additon operation',t)
		operand,value=t.split("+")
		operand=(operand.split(":")[0]).strip()
		value=int(value.strip())
		print(operand,value)
		temp=tempvardict[operand]
		temp+=value
		tempvardict[operand]=temp

	if("-" in t):
		print('subtraction operation',t)
		operand,value=t.split("-")
		operand=(operand.split(":")[0]).strip()
		value=int(value.strip())
		print(operand,value)
		temp=tempvardict[operand]
		temp-=value
		tempvardict[operand]=temp

	if("*" in t):
		print('multilplication operation',t)
		operand,value=t.split("*")
		operand=(operand.split(":")[0]).strip()
		value=int(value.strip())
		print(operand,value)
		temp=tempvardict[operand]
		temp*=value
		tempvardict[operand]=temp

	if("/" in t):
		print('division operation',t)
		operand,value=t.split("/")
		operand=(operand.split(":")[0]).strip()
		value=int(value.strip())
		print(operand,value)
		temp=tempvardict[operand]
		temp/=value
		tempvardict[operand]=temp


# print(indexes)
# print(var)

t=var.split(' ')

for i in range(0,len(t),2):
	vardict[t[i]]=t[i+1]

for i in range(2,len(l)):
	temp=l[i].strip()
	
	if(temp==''):
		data.append(res)
		res=[]
		t_count+=1

	else:
		res.append(l[i].strip())
		tot+=1

t_count+=1
data.append(res)

for i in range(t_count):
	m,n=data[i][0].split(' ')
	lengths[m]=n
	transdict[i]=m
	# data[i].pop(0)
	# tot-=1

# print('Transaction count is ',t_count)
# print('Total instruction present is ',tot)
# print(lengths)

i=0
c_count=0

while i<tot:
	cursor=indexes[c_count]
	max_len=int(lengths[transdict[c_count]])

	# print('Transaction is ',transdict[c_count])
	# print('--------------------------------------------------------------------------------------')
	inc=0

	j=0
	while (j<x):

		t_index=cursor+j
		if(t_index>=max_len):
			break
		else:

			if(t_index==0):
				j=0
				cursor+=1
				log.append("<START "+transdict[c_count]+" >")

				print("<START "+transdict[c_count]+" >")
				printme()
				continue

			# print(data[c_count][t_index])
			do_ops(transdict[c_count],data[c_count][t_index])
			inc+=1
			j+=1

	indexes[c_count]=cursor+inc
	# print(indexes)
	c_count=(c_count+1)%t_count
	if(inc==0):
		inc=1
	i=i+inc

print('Log printing ')
for i in log:
	print(i)
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
vardict={}
tot=0
lengths={}
transdict={}
indexes=[0]*x

def do_ops(transaction,t):
	print(transaction,t)

print(indexes)
print(var)

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
	data[i].pop(0)
	tot-=1

print('Transaction count is ',t_count)
print('Total instruction present is ',tot)
print(lengths)

i=0
c_count=0

while i<tot:
	cursor=indexes[c_count]
	max_len=int(lengths[transdict[c_count]])

	# print('Transaction is ',transdict[c_count])
	# print('--------------------------------------------------------------------------------------')
	inc=0

	for j in range(x):
		t_index=cursor+j
		if(t_index>=max_len):
			break
		else:
			print(data[c_count][t_index])
			inc+=1
	indexes[c_count]=cursor+inc
	print(indexes)
	c_count=(c_count+1)%t_count
	if(inc==0):
		inc=1
	i=i+inc

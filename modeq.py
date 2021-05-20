def check(n,m):
	c=0
	for i in range(1,n+1):
		for j in range(i+1,n+1):
			if ((m%i)%j)==((m%j)%i):
				c+=1
	return c 
n=int(input()) 
for x in range(n):
	n,m=[int(x) for x in input().rstrip().split()]
	print(check(n,m))
n=int(input())
for x in range(n):
	n,p,k=[int(x) for x in input().rstrip().split()]
	s=1
	c,cc,m=0,0,0
	while(s!=p):
		s=cc*k+m
		if s>n: 
			m+=1
			cc=0
			continue
		cc+=1
		c+=1
	print(c-1)

# n=int(input())
# for x in range(n):
# 	n,p,k=[int(x) for x in input().rstrip().split()]
# 	s=1
# 	c,cc,m=0,0,0
# 	while(s!=p):
# 		s=cc*k+m
# 		if s>n: 
# 			m+=1
# 			cc=0
# 			continue
# 		cc+=1
# 		c+=1
# 	print(c-1)

n=int(input())
for x in range(n):
	num,p,k=[int(x) for x in input().rstrip().split()]
	mul=(num-1)//k
	c,pp=0,p%k
	c+=mul*(pp)
	if k*mul+pp-1<num: 
		c+=pp
	else:
		c+=num-k*mul
	c+=p//k+1
	print(c)
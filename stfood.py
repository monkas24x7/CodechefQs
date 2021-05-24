def check(s,p,v):
	if p%(s+1)==0:
		return (p//(s+1))*v
	else:
		return (p//(s+1))*v
t=int(input())
for x in range(t):
	n=int(input())
	best=0
	for y in range(n):	
		s,p,v=[int (x) for x in input().rstrip().split()]
		if check(s,p,v)>best: best=check(s,p,v)
	print(best)
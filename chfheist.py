import numpy as np
def check(D,d,p,q):
	n=int(D/d)
	rem=D%d
	total=int(n*p+n*(n-1)*q/2)*d
	if rem!=0:
		total+=(p+n*q)*(D%d)
	return total 
n=int(input())
for x in range(n):
	D,d,p,q= [int(x) for x in input().rstrip().split()]
	print(check(D,d,p,q))
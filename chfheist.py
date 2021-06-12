def check(D,d,p,q):
	n=D//d
	rem=D%d
	total=(((n*p+(((n**2-n)*q)//2))*d)+(rem*(p+(n*q))))
	return total 
n=int(input())
for x in range(n):
	D,d,p,q= [int(x) for x in input().rstrip().split()]
	print(check(D,d,p,q))
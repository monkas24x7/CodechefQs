def check(xa,xb,Xa,Xb):
	return int(Xa/xa+Xb/xb)
n=int(input())
for x in range(n):
	xa,xb,Xa,Xb=[int(x) for x in input().rstrip().split()]
	print(check(xa,xb,Xa,Xb))

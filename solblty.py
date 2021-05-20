def hehe(x,a,b):
	return (a+(100-x)*b)*10
n=int(input())
for i in range(n):
	nn=[int(x) for x in input().rstrip().split()]
	print(hehe(nn[0],nn[1],nn[2]))

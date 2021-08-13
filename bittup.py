import itertools
def zero(x):
	x=list(x)
	a=x[0]
	for m in x:
		if ~m in x:
			return True
	return False
def check(n,m):
	arr=list(itertools.permutations(range(int(1<<m)),n))
	arr=[x for x in arr if zero(x)]
	return len(arr)%(10**9+7)
n=int(input())
for x in range(n):
	n,m=[int(x) for x in input().rstrip().split()]
	print(check(n,m))
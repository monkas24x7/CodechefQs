def calc(a):
	return ("2","1")[sum(a[0:3])>sum(a[3:6])]
n=int(input())
for x in range(n):
	print(calc([int(x) for x in input().rstrip().split()]))

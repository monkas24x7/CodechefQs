def calc(a):
	aa=set(a)
	if len(aa)>=3: return 2
	elif len(aa)==2:
		if a.count(a[0])==2:
			return 2
		else: return 1
	else: return 0
n=int(input())
for x in range(n):
	print(calc(input().rstrip().split()))

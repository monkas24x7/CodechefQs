def check(arr):
	a=0
	b=0
	for x in range(len(arr)):
		if x%2==0:
			a+=arr[x]
		else:
			b+=arr[x]
		if a==len(arr)-1 and b<=(x+1)//2:
			return x+1
	return x+1
t=int(input())
for x in range(t):
	n=int(input())
	arr=[int(a) for a in input().rstrip().split()]
	print(check(arr))
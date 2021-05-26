def check(arr):
	size=len(arr)//2
	for x in range(len(arr)):
		if sum(arr[0:x+1:2])+size-(x+1)//2<sum(arr[1:x+1:2]) or sum(arr[1:x+1:2])+size-(x+1)//2<sum(arr[0:x+1:2]):
			return x+1
	return x+1
t=int(input())
for x in range(t):
	n=int(input())
	arr=[int(x) for x in list(input())]
	print(check(arr))
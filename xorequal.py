def check(n):
	return int(1<<(n-1))%(10**9+7)
n=int(input())
for x in range(n):
	print(check(int(input())))
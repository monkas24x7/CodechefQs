def hehe(n,x,k):
	if x%k==0 or (n+1-x)%k==0 :
		return True
	return False
n=int(input())
for i in range(n):
	nn=[int(x) for x in input().rstrip().split()]
	if hehe(nn[0],nn[1],nn[2]): print("YES")
	else: print("NO") 

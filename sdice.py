def check(num):
	m=num//4
	m2=num%4
	if m==0:
		if m2==0:
			return 0
		elif m2==1:
			return 20
		elif m2==2:
			return 36
		elif m2==3:
			return 51
	else:	
		if m2==0:
			return ((m-1)*44)+60
		elif m2==1:
			return m*44+32
		elif m2==2:
			return (m+1)*44 
		elif m2==3:
			return (m*44)+55
n=int(input())
for x in range(n):
	num=int(input())
	ans=check(num)
	print(ans)

def factors(x):
	c=[1]
	for i in range(2,x//2+1):
		if x%i==0:
			c.append(i)
	return c
def calc(num):
	total=0
	for x in range(2,num+1):
		num//x
	return total
n=int(input())
for i in range(n):
	num=int(input())
	print(calc(num))
print(factors(10**9))
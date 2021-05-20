import re
def check(inp,string):
	if re.search("\\*"*inp[1],string):
		return "YES"
	return "NO"
n=int(input())
for x in range(n):
	inp=[int(x) for x in input().rstrip().split()]
	string=input()
	ans=check(inp,string)
	print(ans)
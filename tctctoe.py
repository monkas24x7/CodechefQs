def winCon(arr,char):
	match=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[6,4,2],[0,3,6],[1,4,7],[2,5,8]]
	for x in match:
		if arr[x[0]]==char and arr[x[1]]==char and arr[x[2]]==char:
			return True
	return False
def check(arr):
	if arr.count("X")==arr.count("O") or arr.count("X")==arr.count("O")+1:
		if winCon(arr,"O"):
			if winCon(arr,"X"):
				return 3
			if arr.count("X")==arr.count("O"):
				return 1 
		if winCon(arr,"X") :
			if arr.count("X")==arr.count("O")+1:
				return 1
		if not winCon(arr,"O") and not winCon(arr,"X") :
			if arr.count("X")==5 and arr.count("O")==4:
				return 1
			return 2
	return 3
n=int(input().rstrip())
for x in range(n):
	arr=[]
	for y in range(3):
		h=list(input().rstrip())
		arr+=h
	print(check(arr))

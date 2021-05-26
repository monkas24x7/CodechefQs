nums=[2,7,11,15]
target=9
dic={}
def twoSum(nums, target):
	for x in range(len(nums)):
		if str(target-nums[x]) in  dic.keys():
			print ([dic[str(target-nums[x])],x])
		dic[str(nums[x])]=x 
twoSum(nums,target) 
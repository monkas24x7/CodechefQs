dic={}
def twoSum(self, nums: List[int], target: int) -> List[int]:
	for x in nums:
		if str(target-x) in  
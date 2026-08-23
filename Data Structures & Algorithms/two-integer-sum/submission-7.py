class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            first=target-nums[i]
            if first in hash:
                return [hash[first], i]
            hash[nums[i]]=i
        

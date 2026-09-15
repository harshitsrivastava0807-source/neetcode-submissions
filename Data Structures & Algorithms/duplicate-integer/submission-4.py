class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range (i,len(nums)):
                if (num[i]==num[j]):
                    return true
                else:
                    return false
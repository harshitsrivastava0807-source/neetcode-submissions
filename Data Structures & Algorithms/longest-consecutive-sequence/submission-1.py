class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        c,r=0,0
        for i in range(len(nums)):
            if (nums[i]+1)==nums[i+1]:
                c+=1
            else:
                c=0
            if c>r:
                r=c
        return r
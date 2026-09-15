class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s1={}
        for i in range(len(nums)):
            s1[nums[i]]=1+s1.get(nums[i],0)
        s1=sorted(s1.items(),key=lambda item:item[1],reverse=True)
        value=list(s1.values())
        v=[]
        for i in range(k):
            v=value[i]
        return v
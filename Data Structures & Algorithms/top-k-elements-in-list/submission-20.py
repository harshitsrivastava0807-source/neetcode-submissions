class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s1={}
        for i in nums:
            s1[i]=1+s1.get(i,0)    
        v=[[] for i in range(len(nums)+1)]
        for i,j in s1.items():
            v[j].append(i)
        ret=[]
        for i in range(len(v)-1,0,-1):
            for j in v[i]:
                ret.append(j)
                if len(ret)==k:
                    return ret
        
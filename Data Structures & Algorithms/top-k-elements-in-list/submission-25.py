class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s1={}
        for i in nums:
            s1[i]=1+s1.get(i,0)
        sorted_items = sorted(s1.items(), key=lambda x: x[1], reverse=True)
        result = [x[0] for x in sorted_items[:k]]
        return result
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret=[]
        for i in range(1,len(numbers)):
            if (numbers[i-1]+numbers[i])==target:
                ret.append(i-1,i)
                return ret
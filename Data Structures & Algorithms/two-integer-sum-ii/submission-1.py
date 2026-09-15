class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)):
            if (numbers[i-1]+numbers[i])==target:
                return i-1,i
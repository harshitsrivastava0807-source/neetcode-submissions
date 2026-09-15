class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)):
            j=i
            if (numbers[i-1]+numbers[j])==target:
                return [numbers[i-1],numbers[j]]
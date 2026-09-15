class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n1,n2,i1,i2=0,0,0,0
        for i in range(len(heights)):
            if n1<heights[i]:
                n1=heights[i]
                i1=i
        heights.remove(n1)
        for i in range(len(heights)):
            if n2<heights[i]:
                n2=heights[i]
                i2=i
        i=i1-i2
        return n2*i



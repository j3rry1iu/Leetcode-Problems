class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0 
        end = len(height) - 1
        prod = -(inf)
        while start < len(height) and end > 0:
            if prod < min(height[start], height[end]) * (end - start):
                prod = min(height[start], height[end]) * (end - start)
            if height[start] > height[end]:
                end-=1
            else: 
                start+=1
        return prod
            

        
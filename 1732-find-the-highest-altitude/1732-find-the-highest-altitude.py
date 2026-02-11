class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxPoint = 0
        sum = 0
        for i in range(len(gain)):
            sum = sum + gain[i]
            if maxPoint < sum: 
                maxPoint = sum
        return maxPoint

        
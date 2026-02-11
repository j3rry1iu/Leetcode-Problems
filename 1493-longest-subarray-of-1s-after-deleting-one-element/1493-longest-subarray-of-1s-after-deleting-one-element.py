class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, maxLength, count = 0, 0 , 0 
        for right in range(len(nums)): 
            if nums[right] == 0: 
                count += 1
            while count > 1: 
                if nums[left] == 0: 
                    count -= 1
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength
        
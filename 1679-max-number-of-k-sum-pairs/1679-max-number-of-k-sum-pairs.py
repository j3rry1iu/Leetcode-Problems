class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        count = 0
        nums.sort()
        while start < end: 
            sum = nums[start] + nums[end]
            if sum > k: 
                end -= 1
            elif sum < k: 
                start += 1
            elif sum == k: 
                start+=1
                end-=1
                count += 1
        return count
        
                

                
        
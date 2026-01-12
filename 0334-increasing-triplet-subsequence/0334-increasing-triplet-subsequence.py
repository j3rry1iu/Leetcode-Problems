class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = inf
        med = inf
        large = inf
        for i in range(len(nums)):
            if small >= nums[i]: 
                small = nums[i]
            elif med >= nums[i]: 
                med = nums[i]
            else:
                return True
        return False





        
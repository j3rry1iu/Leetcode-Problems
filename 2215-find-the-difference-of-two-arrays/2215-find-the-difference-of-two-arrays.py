class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        distinct1 = set1 - set2
        distinct2 = set2 - set1
        list1 = list(distinct1)
        list2 = list(distinct2)
        return[list1, list2]
        
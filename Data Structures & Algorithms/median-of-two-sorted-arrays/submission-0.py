class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        print(nums)
        mid = len(nums) // 2 + len(nums) % 2
        return nums[mid - 1]  if len(nums) % 2 == 1 else (nums[mid - 1] + nums[mid])/ 2
        
        
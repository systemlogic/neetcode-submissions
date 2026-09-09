class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        self.low = 2 ** 63
        while low <= high:
            mid = low + (high - low) // 2
            self.low = min(self.low, nums[mid])
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return self.low
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if target == nums[mid]: return mid
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid 
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high - 1]:
                    low = mid + 1
                else:
                    high = mid 
        return -1  
        
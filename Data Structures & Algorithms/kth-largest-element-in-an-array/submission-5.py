import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        nums.sort()
        return nums[-k]    
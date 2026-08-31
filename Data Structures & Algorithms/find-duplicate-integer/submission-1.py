class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        _set = set()
        for num in nums:
            if num not in _set:
                _set.add(num)
            else:
                return num
        
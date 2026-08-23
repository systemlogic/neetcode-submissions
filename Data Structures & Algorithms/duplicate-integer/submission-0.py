class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for num in nums:
            if num not in _set:
                _set.add(num)
            else:
                return True
        return False
        
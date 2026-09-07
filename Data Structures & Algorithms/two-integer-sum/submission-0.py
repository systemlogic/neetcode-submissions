class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        index = 0
        for num in nums:
            if num not in _map:
                _map[target - num] = index
            else:
                return [_map[num], index]
            index += 1
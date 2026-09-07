import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = {}
        for num in nums:
            _map[num] = _map.get(num, 0) + 1

        arr = []
        for key in _map:
            heapq.heappush_max(arr, (_map[key], key))
        
        item = []
        for _ in range(k):
            item.append(heapq.heappop_max(arr)[1])
        return item

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) != 1:
            item_1 = heapq.heappop_max(stones)
            item_2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(item_1 - item_2))
        return heapq.heappop_max(stones)

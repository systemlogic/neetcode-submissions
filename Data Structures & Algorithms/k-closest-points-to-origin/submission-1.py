import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for x, y in points:
            dis = (x**2 + y**2)**0.5
            heapq.heappush(lst, (dis, [x, y]))

        arr = []
        for _ in range(k):
            _, (x, y) = heapq.heappop(lst)
            arr.append([x, y])
        return arr
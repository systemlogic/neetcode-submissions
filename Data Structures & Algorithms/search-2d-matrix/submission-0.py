class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for row in matrix:
            lst += row
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = left + (right- left) // 2
            if target == lst[mid]: return True
            elif target < lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
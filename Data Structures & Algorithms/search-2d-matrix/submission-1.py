class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        mid_point = 0
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                mid_point = mid
                break
        
        print(matrix[mid_point])
        lst = matrix[mid_point]
        left, right = 0, len(lst) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target == lst[mid]:
                return True
            elif target > lst[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
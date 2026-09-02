class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        
        water = 0
        while left <= right:
            width = right - left
            if heights[left] < heights[right]:
                water = max(water, width * heights[left])
                left += 1
            else:
                water = max(water, width * heights[right])
                right -= 1
        return water
                

        
class Solution:
    def __init__(self):
        self.combinations = []
        self.combination = []
        

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(self.combination) == len(nums):
            self.combinations.append(self.combination[:])
            return

        for num in nums:
            if num in self.combination:
                continue
            self.combination.append(num)
            self.permute(nums)
            self.combination.pop()
        
        return self.combinations
        
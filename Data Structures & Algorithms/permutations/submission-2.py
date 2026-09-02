class Solution:
    def __init__(self,):
        self.__combination = []
        self.__combinations = []

    def permute(self, nums: List[int], combination = []) -> List[List[int]]:
        if combination and len(nums) == len(combination):
            self.__combinations.append(combination[:])
            return
        
        for num in nums:
            if num in combination: continue
            self.permute(nums, combination + [num])

        return self.__combinations
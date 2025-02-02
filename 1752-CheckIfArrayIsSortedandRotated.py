from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1:] + nums[:i + 1] == sorted(nums)
            
        return True
    

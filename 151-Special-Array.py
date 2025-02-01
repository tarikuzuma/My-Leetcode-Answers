from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        #If the length of the array is 1, return True
        #An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
        #Time Complexity is O(n) where n is the number of elements in nums

        if len(nums) == 1:
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
            
        return True

def test_solution():
    assert Solution().isArraySpecial([1, 2, 3, 4]) == True
    assert Solution().isArraySpecial([1]) == True
    assert Solution().isArraySpecial([2, 1, 4]) == True
    assert Solution().isArraySpecial([4, 3, 1, 6]) == False

if __name__ == "__main__":
    test_solution()
    print("All tests passed.")
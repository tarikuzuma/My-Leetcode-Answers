from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Single pass solution becasue we only need to iterate through the array once
        # Time complexity: O(n)

        n = len(nums)
        longest = 1 
        si = 1
        sd = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                si += 1
                sd = 1
            elif nums[i] < nums[i - 1]:
                sd += 1
                si = 1
            else:
                si = 1
                sd = 1

        return max(longest, si, sd)
    
def TestSolution():
    assert Solution().longestMonotonicSubarray([3,2,1]) == 3, "Test case 1 failed"
    assert Solution().longestMonotonicSubarray([3,3,3,3]) == 1, "Test case 2 failed"
    assert Solution().longestMonotonicSubarray([1,4,3,3,2]) == 2, "Test case 3 failed"

    print("All test cases pass")

if __name__ == "__main__":
    TestSolution()

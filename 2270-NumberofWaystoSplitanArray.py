from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        valid_splits = 0
        prefix_sum = 0

        # Loop therough the lsit without the last element
        for i in range(n-1):

            # Update the prefix sum based on the current element
            prefix_sum += nums[i]

            # if the prefix sum is greater than the total sum, then we can't split the array
            if prefix_sum >= total_sum - prefix_sum:
                valid_splits += 1

        return valid_splits

def TestSolution():
    assert Solution().waysToSplitArray(10,4,-8,7) == 2
    assert Solution().waysToSplitArray([2,3,1,0]) == 2

if __name__ == "__main__":
    TestSolution()
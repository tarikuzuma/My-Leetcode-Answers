from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Algorithm will read if the next element in the array is greater than the current element.
        # If it is, we will add the next element to the current sum.
        # If it is not, we will reset the sum to the current element.
        # Time complexity: O(n)

        n = len(nums)
        max_sum = nums[0]

        current_sum = nums[0]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum
    
def TestSolution():
    assert Solution().maxAscendingSum([10,20,30,5,10,50]) == 65, "Test case 1 failed"
    assert Solution().maxAscendingSum([10,20,30,40,50]) == 150, "Test case 2 failed"
    assert Solution().maxAscendingSum([12,17,15,13,10,11,12]) == 33, "Test case 3 failed"

    print("All test cases pass")

if __name__ == "__main__":
    TestSolution()
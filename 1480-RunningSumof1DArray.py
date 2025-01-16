from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time Complexity is in 0 of n where n is the number of elements in nums
        temp_sum = 0
        temp_array = []

        for i in range (len(nums)):
            temp_sum += nums[i]
            temp_array.append(temp_sum)

        return temp_array
    

def TestSolution():
    solution = Solution()

    assert solution.runningSum([1,2,3,4]) == [1,3,6,10]
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17]

    print ("All tests passed")

if __name__ == '__main__':
    TestSolution()
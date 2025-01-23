from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        # Time Complexity is O(n*m) where n is the number of elements in nums and m is the number of elements in groups
        # Space Complexity is O(1)
        '''
        The idea is that you iterate through the nums array and check if the elements in the groups array are in the nums array
        If they are, you move the offset to the next element in the nums array and check if the next element in the groups array is in the nums array
        If the elements in the groups array are not in the nums array, return False
        If all the elements in the groups array are in the nums array, return True
        '''
        offset = 0

        for group in groups:
            found = False
            while offset <= len(nums) - len(group):
                if nums[offset:offset + len(group)] == group:
                    found = True
                    offset += len(group)
                    break
                offset += 1
            if not found:
                return False

        return True

def test_solution():
    assert Solution().canChoose([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7]) == False
    assert Solution().canChoose([[1, 2, 3], [3, 4]], [1, 2, 3, 3, 4]) == True
    assert Solution().canChoose([[1, 2], [3, 4]], [1, 2, 3, 4]) == True
    assert Solution().canChoose([[1, 2], [3, 4]], [1, 2, 3, 5]) == False
    assert Solution().canChoose([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]) == True

if __name__ == "__main__":
    test_solution()
    print("All tests passed.")
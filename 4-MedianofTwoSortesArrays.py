from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the two lists
        # leetcode easy qwq
        # sort it
        # if the length of the list is even, return the average of the two middle elements (which is the length of the list divided by 2 and the length of the list divided by 2 - 1)
        # if the length of the list is odd, return the middle element
        nums1.extend(nums2)
        length = len(nums1)
        nums1.sort()
        if length % 2 == 0:
            median = (nums1[length//2] + nums1[length//2 - 1]) / 2
            return median
        else:
            median = nums1[length//2]
            return median


        
def TestSolution():
    assert Solution().findMedianSortedArrays([1,3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1,2], [3,4]) == 2.5
    assert Solution().findMedianSortedArrays([0,0], [0,0]) == 0.0
    assert Solution().findMedianSortedArrays([], [1]) == 1.0
    assert Solution().findMedianSortedArrays([2], []) == 2.0

if __name__ == "__main__":
    TestSolution()
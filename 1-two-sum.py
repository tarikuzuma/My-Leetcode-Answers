

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i
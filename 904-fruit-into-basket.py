from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1
            
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
    
    # time complexity: O(n) cuz we traverse the list once and use a sliding window approach which ensures each element is processed at most twice
    # in other wirds, the time complexity is linear with respect to the number of elements in the input list
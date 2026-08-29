from typing import List

class Solution:
     def plusOne(self, digits: List[int]) -> List[int]: 
         return [int(n) for n in str(int("".join(map(str, digits))) + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))   # should print [1, 2, 4]
    print(sol.plusOne([9]))

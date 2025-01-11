from typing import List

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Time complexity is O(n) where n is the number of characters in s

        # If the length of s is less than k, then it is impossible to construct k palindrome
        if (len(s) < k):
            return False
        
        # If the length of s is equal to k, then it is possible to construct k palindrome
        no = 0

        # Count the number of characters that have odd frequency
        for i in range(26):
            no += s.count(chr(i+97)) % 2
        return no <= k
    
def TestSolution():
    solution = Solution()
    assert solution.canConstruct("annabelle", 2) == True
    assert solution.canConstruct("leetcode", 3) == False
    assert solution.canConstruct("true", 4) == True

    print("All tests passed")

if __name__ == '__main__':
    TestSolution()

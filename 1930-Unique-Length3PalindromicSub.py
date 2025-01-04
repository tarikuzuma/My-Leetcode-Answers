from typing import List

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        Iterate through each unique character in the string s using set(s).
        Use find() and rfind() to determine the first and last occurrence of the character.
        Count the unique middle characters between the first and last positions using set().
        Sum up the counts for all unique characters.
        Credits to "https://leetcode.com/u/suhas_sr7/" for the solution.
        '''

        count = 0
        for c in set(s):
            first = s.find(c)
            last = s.rfind(c)
            count += len(set(s[first+1:last]))
        print(count)
        return count
    
def TestSolution():
    assert Solution().countPalindromicSubsequence("aabca") == 3
    assert Solution().countPalindromicSubsequence("adc") == 0
    assert Solution().countPalindromicSubsequence("bbcbaba") == 4


if __name__ == "__main__":
    TestSolution()    
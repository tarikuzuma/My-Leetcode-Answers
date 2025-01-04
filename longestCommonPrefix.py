from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string = min(strs)
        max_string = max(strs)

        for i in range (len(min_string)):
            if min_string[i] != max_string[i]:
                return min_string[:i]
            
        return min_string
    
# Test cases
s = Solution()
print(s.longestCommonPrefix(["car","racecar","potcar"])) # Output: "fl"
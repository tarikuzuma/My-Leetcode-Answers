class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        # a to i are represented as 1 to 9
        # j to z are represented as 10# to 26#

        # Time complexity is O(n) where n is the number of characters in s

        output = ""
        i = 0

        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                output += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                output += chr(int(s[i]) + 96)
                i += 1

        return output
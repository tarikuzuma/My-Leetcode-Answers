'''
   13.  Roman to Integer Problem Leetcode
'''

'''
    My idea solution is to contain a dictionary with the roman numerals and their corresponding integer values.
    For ex:
        M = 1000
        D = 500
        C = 100
        L = 50
        X = 10
        V = 5
        I = 1

    And then an algorithm to check if the number before the current number is less than the current number, so we subtract it by the designated roman numberal.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        total = 0
        while i < len(s):
            # Ensure the character is in the dictionary before accessing it
            if s[i] in roman_numerals:
                value = roman_numerals[s[i]]
                if i+1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                    total -= value
                else:
                    total += value
                i += 1
            else:
                raise KeyError(f"Invalid Roman numeral character: {s[i]}")
        return total
    
# Example:
s = Solution()
print(s.romanToInt("III")) # 3
class Solution:
    def isValid(self, s: str) -> bool:
        accepted_parenthesis = ["()", "{}", "[]"]
        while any(parenthesis in s for parenthesis in accepted_parenthesis):
            for parenthesis in accepted_parenthesis:
                s = s.replace(parenthesis, "")
        return not s

# Test cases
s = Solution()
print(s.isValid("()[]{}")) # Output: True
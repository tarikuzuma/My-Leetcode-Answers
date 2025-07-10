class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch.isdigit():
                stack.pop()

            else:
                stack.append(ch)

        return "".join(stack)
    
def TestSolution():
    assert Solution().clearDigits("123abc") == "123", "Test case 1 failed"
    assert Solution().clearDigits("abc123") == "", "Test case 2 failed"
    assert Solution().clearDigits("abc") == "", "Test case 3 failed"

    print("All test cases pass")

if __name__ == "__main__":
    TestSolution()
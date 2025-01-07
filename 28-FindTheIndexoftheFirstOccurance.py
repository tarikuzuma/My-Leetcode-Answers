class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time complexity in O(N∗M)
        if needle not in haystack:
            return -1
        else:
            return 0 if len(needle) == 0 else haystack.index(needle)
        
def TestSolution():
    assert Solution().strStr("hello", "ll") == 2, "Test case 1 failed"
    assert Solution().strStr("aaaaa", "bba") == -1, "Test case 2 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution() 
    # solution = Solution()
    # string = "czuu"
    # queues = [[0, 0, 0], [1, 1, 1]]
    # solution.shiftingLetters(string, queues)
        
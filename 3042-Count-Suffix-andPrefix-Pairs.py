from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Start from index 1
        # Compare the current word with the previous word
        # If the current word is a prefix of the previous word, increment the count

        count = 0 

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1

        return count

    
def TestSolution():
    assert Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"]) == 4, "Test case 1 failed"
    assert Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"]) == 2, "Test case 2 failed"
    assert Solution().countPrefixSuffixPairs(["abab","ab"]) == 0, "Test case 3 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution() 
    # solution = Solution()
    # string = "czuu"
    # queues = [[0, 0, 0], [1, 1, 1]]
    # solution.shiftingLetters(string, queues)
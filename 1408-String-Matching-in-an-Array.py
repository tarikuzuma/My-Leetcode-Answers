from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #  O(n^2 * m) where n is the number of words and m is the length of the word
        # Use hash set to store the result
        result = set()
        n = len(words)

        # Loop through the list of words
        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[i] in words[j]:
                        result.add(words[i])
        return list(result)
    
def TestSolution():
    assert Solution().stringMatching(["mass","as","hero","superhero"]) == ["as","hero"], "Test case 1 failed"
    assert Solution().stringMatching(["leetcode","et","code"]) == ["et","code"], "Test case 2 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution() 
    # solution = Solution()
    # string = "czuu"
    # queues = [[0, 0, 0], [1, 1, 1]]
    # solution.shiftingLetters(string, queues)
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # This problem is a joke in python
        
        # Time copelxity in the worst case is O(n) where n is the number of words
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1

        return count
    

def TestSolution():
    solution = Solution()
    assert solution.prefixCount(["a","aba","ababa","aa"], "a") == 4, "Test case 1 failed"
    assert solution.prefixCount(["pa","papa","ma","mama"], "p") == 2, "Test case 2 failed"
    assert solution.prefixCount(["abab","ab"], "ab") == 2, "Test case 3 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution()

'''
Java:

import java.util.List;
import java.util.ArrayList;

class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
                count++;
            }
        }
        return count;
    }
}
'''
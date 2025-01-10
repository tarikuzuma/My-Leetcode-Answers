from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def sol1():
            # Time complexity is O(n) where n is the number of words in words1

            ans = set(words1)

            # Count the frequency of each letter in words2
            freq = {}

            for word in words2:
                for c in word:
                    count = word.count(c)
                    if c not in freq:
                        freq[c] = count
                    else:
                        freq[c] = max(freq[c], count)

            # Check if the word in words1 has the frequency of each letter in words2
            for word in words1:
                for c in freq:
                    if word.count(c) < freq[c]:
                        ans.remove(word)
                        break
            
            return list(ans)
        

        def sol2():
            # Time complexity is O(n) where n is the number of words in words1
            # Temproary List that checks if the first letter in words2 is present in words1, then the enxt letter and so on
            temp = [0]*26

            # Loop throuhg eall letters in words2

            for word in words2:
                temp2 = [0] * 26
                for letter in word:
                    temp2[ord(letter) - ord('a')] += 1
                for i in range(26):
                    temp[i] = max(temp[i], temp2[i])

            # Now we have the maximum count of each letter in words2
            ans = []
            for word in words1:
                temp2 = [0] * 26
                for letter in word:
                    temp2[ord(letter) - ord('a')] += 1
                if all(temp2[i] >= temp[i] for i in range(26)):
                    ans.append(word)
            return ans

        

                    
    
    
    
def TestSolution():
    solution = Solution()
    assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]) == ["facebook","google","leetcode"], "Test case 1 failed"
    assert solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]) == ["apple","google","leetcode"], "Test case 2 failed"

    print("All test cases pass")

    
    

if __name__ == "__main__":
    TestSolution()

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Get the vowels of the string
        # Save every vowel in the list 
        # Reverse the list
        # Replace the vowels in the string with the reversed list

        vowels = "aeiouAEIOU"
        vowels_list = [char for char in s if char in vowels]
        vowels_list.reverse()
        result = ""
        for char in s:
            if char in vowels:
                result += vowels_list.pop(0)
            else:
                result += char
        return result

    
def test_solution():
    s = Solution()
    print (s.reverseVowels("hello"))
    print (s.reverseVowels("leetcode"))

if __name__ == "__main__":
    test_solution()

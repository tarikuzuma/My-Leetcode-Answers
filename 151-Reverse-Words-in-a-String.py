class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()[::-1]
        x_reversed_list = list[::-1]
        return " ".join(x_reversed_list)
    
    def reverseWords2(self, s:str) -> str:
        original_to_array = s.split()
        original_to_array.reverse()
        return " ".join(original_to_array)
    
def test_solution():
    Solution().reverseWords2("the sky is blue")

if __name__ == "__main__":
    test_solution()
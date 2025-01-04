class Solution:
    def mergeAlernately(self, word1: str, word2: str) -> str:
        str1 = list(word1)
        str2 = list(word2)

        result = []

        while str1 and str2:
            result.append(str1.pop(0))
            result.append(str2.pop(0))

        return "".join(result) + "".join(str1) + "".join(str2)
    
def test_solution():
    s = Solution()
    assert s.mergeAlernately("abc", "pqr")
    assert s.mergeAlernately("ab", "pqrs")
    assert s.mergeAlernately("abcd", "pq")
    assert s.mergeAlernately("ab", "pq")


if __name__ == "__main__":
    test_solution()
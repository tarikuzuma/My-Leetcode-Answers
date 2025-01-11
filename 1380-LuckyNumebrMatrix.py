from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        # Time complexity is O(n*m) where n is the number of rows and m is the number of columns
        #PLot both lsits to get the minimum and maximum values
        min_values = [min(row) for row in matrix]
        max_values = [max(row) for row in zip(*matrix)]

        #Return the intersection of the two lists
        return list(set(min_values) & set(max_values))

def TestSolution():
    solution = Solution()
    assert solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]) == [15]
    assert solution.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]) == [12]
    assert solution.luckyNumbers([[7,8],[1,2]]) == [7]
    print("All tests passed")

if __name__ == '__main__':
    TestSolution()
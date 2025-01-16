from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Time Complexity is in 0 of n where n is the number of elements in accounts

        temp_array = []
       
        for i in range (len(accounts)):
            temp_sum = 0
            for account in accounts[i]:
                temp_sum += account

            temp_array.append(temp_sum)

        return max(temp_array)
    

def TestSolution():
    solution = Solution()

    assert solution.maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert solution.maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17

    print ("All tests passed")
if __name__ == '__main__':
    TestSolution()

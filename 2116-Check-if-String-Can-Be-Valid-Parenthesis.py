class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        # Time complexity is O(n) where n is the number of characters in s
        string_length = len(s)

        if string_length % 2 != 0:
            return False
        
        open_count = 0
        for i in range(string_length):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1  
            else:
                open_count -= 1  # Closing bracket
            if open_count < 0: 
                return False
            
        close_count = 0
        for i in range(string_length-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
            
        return True
    
         
def TestSolution():
    solution = Solution()

    assert solution.canBeValid("))()))", "010100") == True
    assert solution.canBeValid("()()", "0000") == True
    assert solution.canBeValid(")", "0") == False

    print ("All tests passed")

if __name__ == '__main__':
    TestSolution()


from typing import List
'''
    This problem was so hard that I had to look at the solution to understand it. The solution is based on the concept of a difference array. 
    https://www.youtube.com/watch?v=jJdUJoiqdmQ
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        # Dummy element to avoid index out of range. Difference array to store the total shifts for each character.
        diff_array = [0] * (n + 1) 

        # 1. Make the difference array
        for shift in shifts:
            if shift[2] == 1:
                diff_array[shift[0]] += 1
                diff_array[shift[1] + 1] -= 1
            else:
                diff_array[shift[0]] -= 1
                diff_array[shift[1] + 1] += 1

        # 2. Calculate the cumultiive shifts

        # cumulitive shifts array to store the total shifts for each character.
        cumilitive_shifts = [0] * n
        current_shift = 0

        # Calculate the cumilitive shifts for each character
        for i in range(n):
            current_shift += diff_array[i]
            cumilitive_shifts[i] = current_shift

        # 3. Shift the characters
        shifted_string = ""
        for i in range(n):
            shifted_string += chr((ord(s[i]) - ord('a') + cumilitive_shifts[i]) % 26 + ord('a'))

        # print (shifted_string)
        return shifted_string
    

def TestSolution():
    assert Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace", "Test case 1 failed"
    assert Solution().shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz", "Test case 2 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution() 
    # solution = Solution()
    # string = "czuu"
    # queues = [[0, 0, 0], [1, 1, 1]]
    # solution.shiftingLetters(string, queues)
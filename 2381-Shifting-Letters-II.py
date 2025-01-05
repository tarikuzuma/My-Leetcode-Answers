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

        # This loop shifts the characters by the cumilitive shifts based on the remainder of the shifts
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



'''
Java:
class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        
        // Step 1: Create the difference array
        int[] diffArray = new int[n + 1];
        for (int[] shift : shifts) {
            if (shift[2] == 1) { // Right shift
                diffArray[shift[0]] += 1;
                diffArray[shift[1] + 1] -= 1;
            } else { // Left shift
                diffArray[shift[0]] -= 1;
                diffArray[shift[1] + 1] += 1;
            }
        }
        
        // Step 2: Calculate the cumulative shifts
        int[] cumulativeShifts = new int[n];
        int currentShift = 0;
        for (int i = 0; i < n; i++) {
            currentShift += diffArray[i];
            cumulativeShifts[i] = currentShift;
        }
        
        // Step 3: Shift the characters in the string
        StringBuilder shiftedString = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int newChar = (s.charAt(i) - 'a' + cumulativeShifts[i]) % 26;
            if (newChar < 0) {
                newChar += 26; // Handle negative shifts to wrap around
            }
            shiftedString.append((char) ('a' + newChar));
        }
        
        // Return the final shifted string
        return shiftedString.toString();
    }
}

'''
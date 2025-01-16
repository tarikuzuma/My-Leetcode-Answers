from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        output = []

        for i in range (1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))

        return output
    

def TestSolution():
    solution = Solution()

    assert solution.fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert solution.fizzBuzz(1) == ["1"]
    assert solution.fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
    
    print ("All tests passed")  

if __name__ == '__main__':
    TestSolution()
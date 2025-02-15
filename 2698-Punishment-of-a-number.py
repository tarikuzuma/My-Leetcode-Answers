class Solution:
    def punishment(self, n: str) -> str:
        # Thanks Nikhil for the array xd
        punishable = [1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,
                      657,675,703,756,792,909,918,945,964,990,991,999,1000]
        
        total = 0

        # So a punishable number is a number that is less than or equal to n
        for num in punishable:
            if num <= n:
                # We add the square of the number to the total because the problem states thats the punihsment lol
                total += num * num
            else:
                break

        return total
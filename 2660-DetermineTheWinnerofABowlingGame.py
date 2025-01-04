
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # Red through each element in the list and add them to the total score
        # Multiply the next two elements by 2 in an array if the previous element (which is in an int) in the array is a 10
        #Assumes that each player ahs the same number of elements in their list

        def calculate_score(player):
            player_score = 0
            for i in range(len(player)):
                if i > 0 and player[i-1] == 10:
                    player_score += player[i] * 2
                elif i > 1 and player[i-2] == 10:
                    player_score += player[i] * 2
                else:
                    player_score += player[i]
            return player_score
        
        player1_score = calculate_score(player1)
        player2_score = calculate_score(player2)

        print(player1_score, player2_score)

        if player1_score > player2_score:
            # print ("Player 1 wins")
            return 1
        elif player1_score < player2_score:
            # print("Player 2 wins")
            return 2
        else:
            # print("It's a draw")
            return 0

        
def test_solution():
    assert Solution().isWinner([5,10,3,2], [6,5,7,3]) == 1
    assert Solution().isWinner([3,5,7,6], [8,10,10,2]) == 2
    assert Solution().isWinner([2,3], [4,1]) == 0
    assert Solution().isWinner([1,1,1,10,10,10,10], [10,10,10,10,1,1,1]) == 2
    assert Solution().isWinner([3,6,10,8], [9,9,9,9]) == 2

if __name__ == "__main__":
    test_solution()
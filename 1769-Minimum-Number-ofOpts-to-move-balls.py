from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Algo is in O(n^2) time complexity and O(n) space complexity because of the two loops

        # pos is a list that stores the positions of the 1s in the boxes string
        pos, ans = [], []

        # Find the positions of the 1s in the boxes string
        for i in range(len(boxes)):
            if boxes[i] == '1':
                pos.append(i)
        for i in range(len(boxes)):
            ans.append(sum([abs(i - j) for j in pos]))
        return ans
    
def TestSolution():
    assert Solution().minOperations("110") == [1, 1, 3], "Test case 1 failed"
    assert Solution().minOperations("001011") == [11, 8, 5, 4, 3, 4], "Test case 2 failed"
    
    print("All test cases pass")

if __name__ == "__main__":
    TestSolution() 


# Java:
'''
from java.util.ArrayList;
from java.util.List;

class Solution {
    public List<Integer> minOperations(String boxes) {
        // Algo is in O(n^2) time complexity and O(n) space complexity because of the two loops

        // pos is a list that stores the positions of the 1s in the boxes string
        List<Integer> pos = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();

        // Find the positions of the 1s in the boxes string
        for (int i = 0; i < boxes.length(); i++) {
            if (boxes.charAt(i) == '1') {
                pos.add(i);
            }
        }
        for (int i = 0; i < boxes.length(); i++) {
            int sum = 0;
            for (int j = 0; j < pos.size(); j++) {
                sum += Math.abs(i - pos.get(j));
            }
            ans.add(sum);
        }
        return ans;
    }
}
'''
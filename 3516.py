class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        pos1 = abs(x - z)
        pos2 = abs(y - z)
        
        print (pos1, pos2)
        if pos1 < pos2:
            return 1
        elif pos2 < pos1:
            return 2
        else:
            return 0

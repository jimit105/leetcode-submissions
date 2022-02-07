# https://leetcode.com/problems/rotating-the-box/discuss/1210074/Python3.-Shift-stones-then-rotate

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            move_position = len(row) - 1
            
            for j in range(len(row) - 1, -1, -1):
                if row[j] == '*':
                    move_position = j - 1
                elif row[j] == '#':
                    row[j], row[move_position] = row[move_position], row[j]
                    move_position -= 1
                    
        return list(zip(*box[::-1]))
        

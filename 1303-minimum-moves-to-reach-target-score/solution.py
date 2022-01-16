class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        
        if 1 << maxDoubles == target:
            return maxDoubles

        while target > 1:
            if target % 2 == 0 and maxDoubles:
                target = target >> 1
                moves += 1
                maxDoubles -= 1
            elif not maxDoubles:
                diff = target - 1
                target -= diff
                moves += diff
            else:
                target -= 1
                moves += 1
            print(target, moves)
            

        return moves
        

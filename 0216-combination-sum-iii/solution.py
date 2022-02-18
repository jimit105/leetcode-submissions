# Approach 1 - Backtracking

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(comb.copy())
                return
            elif remain < 0 or len(comb) == k:
                return
            
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain - (i + 1), comb, i + 1)
                comb.pop()
                
        
        results = []
        backtrack(n, [], 0)
        
        return results
                

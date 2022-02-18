# Approach 1 - Backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(remain, comb, next_start):
            if remain == 0:
                results.append(comb.copy())
                return
            elif remain < 0:
                return
            
            for i in range(next_start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
                
        results = []
        backtrack(target, [], 0)
        
        return results
        

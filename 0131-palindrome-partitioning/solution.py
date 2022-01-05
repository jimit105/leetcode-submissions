# DFS using Backtracking

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(start_idx, end_idx):
            while start_idx <= end_idx:
                if s[start_idx] != s[end_idx]: 
                    return False
                start_idx += 1
                end_idx -=1
            return True
                
        
        def dfs(start_idx, path):
            if start_idx >= len(s):
                res.append(path)
                
            for i in range(len(s) - start_idx):
                if isPalindrome(start_idx, start_idx+i):
                    dfs(start_idx+i+1, path + [s[start_idx : start_idx+i+1]])
                    
        dfs(0, [])
        return res
                    
                

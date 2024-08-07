# Approach: Depth First Search
# https://leetcode.com/problems/word-search/discuss/2843501/PythonC%2B%2B-faster-than-99-DFS-(explained) 

from collections import Counter
from itertools import chain

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        if len(word) > m * n:
            return False
        
        # not enough letters on the board
        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False
        
        # Inverse word if it is better to start from the end
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]
            
            
        def dfs(i, j, s):
            if s == len(word):
                return True
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:
                board[i][j] = '#'
                adj = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
                dp = any(dfs(ii, jj, s+1) for ii, jj in adj)
                board[i][j] = word[s]
                return dp
            
            return False
        
        return any(dfs(i, j, 0) for i, j in product(range(m), range(n)))
            
        

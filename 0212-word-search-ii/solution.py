# Approach 1: Backtracking with Trie

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
            
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        
        def backtrack(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)
                
            # mark cell as visited
            board[row][col] = '#'
            
            # explore neighbors in 4 directions
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtrack(newRow, newCol, currNode)
                
            # end of exploration; restore the cell
            board[row][col] = letter
            
            # Optimization: incrementally remove the matched leaf node in Trie
            if not currNode:
                parent.pop(letter)
                
                
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtrack(row, col, trie)
                    
        return matchedWords
        

# Approach: Breadth First Search

# n = len(wordList), l = length of each word
# Time: O(n * 26 * l)
# Space: O(n)

import string
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = word[:i] + c + word[i + 1 :]

                    if next_word in wordList and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

        return 0
        

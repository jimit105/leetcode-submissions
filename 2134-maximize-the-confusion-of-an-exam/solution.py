# Approach 2: Sliding Window

# Time: O(n)
# Space: O(1)

from collections import Counter

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = k
        count = Counter(answerKey[:k])

        left = 0
        for right in range(k, len(answerKey)):
            count[answerKey[right]] += 1

            while min(count['T'], count['F']) > k:
                count[answerKey[left]] -= 1
                left += 1

            max_size = max(max_size, right - left + 1)

        return max_size

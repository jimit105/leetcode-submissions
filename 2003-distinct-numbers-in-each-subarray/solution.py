# Approach 1: Hash Map

# Time: O(n)
# Space: O(n)

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = [0] * (n - k + 1)

        freq = {}

        # Process first window
        for num in nums[:k]:
            freq[num] = freq.get(num, 0) + 1
        answer[0] = len(freq)

        # Slide window and update freq
        for pos in range(k, n):
            left = nums[pos - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

            right = nums[pos]
            freq[right] = freq.get(right, 0) + 1

            answer[pos - k + 1] = len(freq)

        return answer
        

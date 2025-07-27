# Time: O(n)
# Space: O(n)

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates
        filtered = []
        for num in nums:
            if not filtered or filtered[-1] != num:
                filtered.append(num)
        
        count = 0
        for i in range(1, len(filtered) - 1):
            # Hill condition
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1
            # Valley condition
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1

        return count
        

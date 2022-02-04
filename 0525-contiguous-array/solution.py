# Approach 3 - Using HashMap

# Time: O(n)
# Space: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {}
        mapping[0] = -1
        count = 0
        maxlen = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count in mapping:
                maxlen = max(maxlen, i - mapping.get(count))
            else:
                mapping[count] = i
                
        return maxlen
        

# Approach: Sliding Window

# Time: O(n)
# Space: O(n)

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        count = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                count[remove] -= 1
                if count[remove] == 0:
                    count.pop(remove)
            while right < n and len(count) < distinct:
                add = nums[right]
                count[add] = count.get(add, 0) + 1
                right += 1
            if len(count) == distinct:
                res += n - right + 1

        return res

        

# Approach 7: Floyd's Tortoise and Hare (Cycle Detection)

# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the "entrance" to the cycle.
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

            
        

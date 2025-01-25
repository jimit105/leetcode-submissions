# Approach: Sorting + Grouping

# Time: O(n * log n)
# Space: O(n)

from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group

        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])
        
        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                # new group
                curr_group += 1

            num_to_group[nums_sorted[i]] = curr_group

            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        # Iterate through the input and overwrite each element with the next element in its corresponding group
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums

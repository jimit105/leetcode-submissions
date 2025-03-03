# Approach 1: Dynamic Lists

# Time: O(n)
# Space: O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        less.extend(equal)
        less.extend(greater)

        return less
        

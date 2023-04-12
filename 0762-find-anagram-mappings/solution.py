# Approach 2: HashMap

# Time: O(N)
# Space: O(N)

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        value_to_pos = {v: k for k, v in enumerate(nums2)}

        mappings = []
        for num in nums1:
            mappings.append(value_to_pos.get(num))

        return mappings

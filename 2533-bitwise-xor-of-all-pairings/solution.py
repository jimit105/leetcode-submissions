# Approach 2: Space Optimized Bit Manipulation

# n, m = len(nums1), len(nums2)
# Time: O(n + m)
# Space: O(1)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize XOR results for both arrays
        xor1, xor2 = 0, 0

        len1, len2 = len(nums1), len(nums2)

        # If nums2 length is odd, each element in nums1 appears odd times in final result
        if len2 % 2:
            for num in nums1:
                xor1 ^= num

        # If nums1 length is odd, each element in nums2 appears odd times in final result
        if len1 % 2:
            for num in nums2:
                xor2 ^= num

        return xor1 ^ xor2

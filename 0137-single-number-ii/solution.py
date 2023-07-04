# Approach 4: Bit Manipulation

# Time: O(N)
# Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        loner = 0

        for shift in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> shift) & 1

            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        # Do not mistake sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner

# Approach 1: Generate All Subsets Using Backtracking

# Time: O(n * 2^n)
# Space: O(n * 2^n)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(nums, index, subset, subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return

            # Generate subsets with nums[i]
            subset.append(nums[index])
            generate_subsets(nums, index + 1, subset, subsets)
            subset.pop()

            # Generate subsets without nums[i]
            generate_subsets(nums, index + 1, subset, subsets)

        subsets = []
        generate_subsets(nums, 0, [], subsets)

        result = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total

        return result

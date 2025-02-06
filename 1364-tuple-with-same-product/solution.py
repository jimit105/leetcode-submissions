# Approach 3: Product Frequency Hash Map

# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        pair_products_freq = {}
        total_num_of_tuples = 0

        for first_idx in range(n):
            for second_idx in range(first_idx + 1, n):
                product_val = nums[first_idx] * nums[second_idx]

                pair_products_freq[product_val] = pair_products_freq.get(product_val, 0) + 1

            
        for product_freq in pair_products_freq.values():
            pairs_of_equal_product = (product_freq - 1) * product_freq // 2

            total_num_of_tuples += 8 * pairs_of_equal_product

        return total_num_of_tuples
        

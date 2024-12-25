# Approach 2: Hash Table

# n = length of input array, L = no. of non-zeros elements
# Time: O(n) for creating hash table, O(L) for calculating dot product
# Space: O(L) for creating hash map, O(1) for calculating dot product

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzeros[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, num in self.nonzeros.items():
            if i in vec.nonzeros:
                result += num * vec.nonzeros[i]

        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

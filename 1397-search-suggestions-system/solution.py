# Approach - Binary Search
# https://leetcode.com/problems/search-suggestions-system/discuss/2167794/Python-Easy-2-Approaches

# If n is the length of products and m is length of searchWord, then
# Time: O(nlogn + mlogn) - Sorting requires O(nlogn) and O(logn) is for binary search the products for a prefix.
# Space: O(1)

import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ''
        res = []
        i = 0
        
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([word for word in products[:i+3] if word.startswith(prefix)])
        
        return res
        

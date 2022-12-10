# Approach 1: One Pass DFS

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def tree_sum(node):
            if node is None:
                return 0
            left_sum = tree_sum(node.left)
            right_sum = tree_sum(node.right)
            total_sum = left_sum + right_sum + node.val
            all_sums.append(total_sum)
            return total_sum

        total = tree_sum(root)
        ans = 0
        for s in all_sums:
            ans = max(ans, s * (total - s))

        return ans % (10 ** 9 + 7)

# Approach 1: Depth First Search

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if node is None:
                return True

            is_left_uniValue = dfs(node.left)
            is_right_uniValue = dfs(node.right)

            if is_left_uniValue and is_right_uniValue:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False

                self.count += 1
                return True

            return False

        dfs(root)
        return self.count

# Approach: Recursion

# Time: O(n^2)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        # Create root node from first element of preorder
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        # Find the left subtree root in postorder
        # The second element in preorder is the root of left subtree
        left_root_val = preorder[1]
        left_root_index = postorder.index(left_root_val)

        left_size = left_root_index + 1

        left_preorder = preorder[1 : left_size + 1]
        right_preorder = preorder[left_size + 1 :]

        left_postorder = postorder[: left_size]
        right_postorder = postorder[left_size : -1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root
        

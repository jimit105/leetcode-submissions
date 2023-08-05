# Approach 1: Recursive Dynamic Programming

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def all_possible_bst(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]

        for i in range(start, end + 1):
            left_subtree = self.all_possible_bst(start, i - 1, memo)
            right_subtree = self.all_possible_bst(i + 1, end, memo)

            for left in left_subtree:
                for right in right_subtree:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.all_possible_bst(1, n, memo)

# Approach 1: Implementing Parent Pointers

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(curr, parent):
            if curr:
                curr.parent = parent
                add_parent(curr.left, curr)
                add_parent(curr.right, curr)
        add_parent(root, None)

        answer = []
        visited = set()

        def dfs(curr, distance):
            if not curr or curr in visited:
                return
            visited.add(curr)
            if distance == 0:
                answer.append(curr.val)
                return
            dfs(curr.parent, distance - 1)
            dfs(curr.left, distance - 1)
            dfs(curr.right, distance - 1)

        dfs(target, k)

        return answer

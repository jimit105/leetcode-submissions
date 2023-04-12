# Approach: Using Stacks

# Time: O(N), N = number of characters in the original path
# Space: O(N)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for portion in path.split('/'):
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                    stack.append(portion)

        return '/' + '/'.join(stack)



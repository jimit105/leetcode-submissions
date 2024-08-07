# Approach 2: Binary Search Tree (BST) as Bucket


class MyHashSet:
    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]
        
    def _hash(self, key) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)
        
    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Bucket:
    def __init__(self) -> None:
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)


class TreeNode:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None

    
class BSTree:
    def __init__(self) -> None:
        self.root = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.val:
            return root
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
        
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key:int) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

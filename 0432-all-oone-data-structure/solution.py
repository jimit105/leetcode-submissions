# Approach: Using Doubly Linked List

# Time: O(1)
# Space: O(n)

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0) # Dummy head
        self.tail = Node (0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} # Mapping from key to its node
        

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key) # Remove key from current node

            next_node = node.next
            if next_node == self.tail or next_node.freq != freq + 1:
                # Create new node
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                new_node.prev = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                self.map[key] = new_node

            else:
                # Add key in the next node
                next_node.keys.add(key)
                self.map[key] = next_node

            # Remove the current node if it has no keys left
            if not node.keys:
                self._removeNode(node)

        # Key does not exist
        else:
            first_node = self.head.next
            if first_node == self.tail or first_node.freq > 1:
                # Create new node
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.prev = self.head
                new_node.next = first_node
                self.head.next = new_node
                first_node.prev = new_node
                self.map[key] = new_node
            else: # Freq is 1
                first_node.keys.add(key)
                self.map[key] = first_node


    def dec(self, key: str) -> None:
        if key not in self.map:
            return # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                # Creae a new node
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.map[key] = new_node
            else:
                # Decrement the existing previous node
                prev_node.keys.add(key)
                self.map[key] = prev_node

        # Remove node if it has no keys left
        if not node.keys:
            self._removeNode(node)


    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return '' # No keys exist
        return next(iter(self.tail.prev.keys)) # Return one of the keys from tail's prev node
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return '' # No keys exist
        return next(iter(self.head.next.keys)) # Return one of the keys from head's next node


    def _removeNode(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

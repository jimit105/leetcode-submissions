# Approach 1: Two Maps

# Time: O(log n)
# Space: O(n)

from sortedcontainers import SortedSet
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.number_to_indices = defaultdict(SortedSet)
        self.index_to_number = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            previous_num = self.index_to_number[index]
            self.number_to_indices[previous_num].remove(index)
            if not self.number_to_indices[previous_num]:
                del self.number_to_indices[previous_num]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)


    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

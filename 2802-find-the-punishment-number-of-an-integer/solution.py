# Approach 2: Recursion of Strings

# Time: O(n * 2 ^ (log n))
# Space: O(log n)

class Solution:
    def can_partition(self, string_num, target):
        # Valid partition
        if not string_num and target == 0:
            return True

        # Invalid partition
        if target < 0:
            return False

        # Recursively check all partitions for a valid partition
        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1 :]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_sum = 0

        for current_num in range(1, n + 1):
            squared_num = current_num * current_num

            if self.can_partition(str(squared_num), current_num):
                punishment_sum += squared_num

        return punishment_sum
        

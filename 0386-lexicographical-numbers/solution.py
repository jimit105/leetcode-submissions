# Approach 2: Iterative Approach

# Time: O(n)
# Space: O(1)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current_num = 1

        for _ in range(n):
            result.append(current_num)

            # If we can multiply by 10, that's the next lexicographical number
            if current_num * 10 <= n:
                current_num *= 10
            # If we can't multiply by 10, we need to increment and handle carry
            else:
                while current_num % 10 == 9 or current_num + 1 > n:
                    current_num //= 10
                current_num += 1

        return result
        

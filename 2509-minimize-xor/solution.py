# Approach 2: Building the Answer

# Time: O(log n)
# Space: O(1)

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count('1')
        set_bits_count = 0
        current_bit = 31 # Start from most significant bit

        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (target_set_bits_count - set_bits_count > current_bit):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1

        return result


    # Helper function to check if the given bit position in result is set (1).
    def _is_set(self, x, bit):
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in result to 1.
    def _set_bit(self, x, bit):
        return x | (1 << bit)


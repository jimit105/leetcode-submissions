# Approach: Backtracking

# Time: O(n!)
# Space: O(n)

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result_sequence = [0] * (n * 2 - 1)
        is_number_used = [False] * (n + 1)

        self.find_lexicographically_largest_sequence(0, result_sequence, is_number_used, n)

        return result_sequence

    def find_lexicographically_largest_sequence(self, current_idx, result_sequence, is_number_used, n):
        if current_idx == len(result_sequence):
            return True

        if result_sequence[current_idx] != 0:
            return self.find_lexicographically_largest_sequence(current_idx + 1, result_sequence, is_number_used, n)

        for number_to_place in range(n, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_idx] = number_to_place

            # If placing number 1, move to the next index directly
            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(current_idx + 1, result_sequence, is_number_used, n):
                    return True

            # Place larger numbers at two positions if valid
            elif (current_idx + number_to_place < len(result_sequence) and result_sequence[current_idx + number_to_place] == 0):
                result_sequence[current_idx + number_to_place] = number_to_place

                if self.find_lexicographically_largest_sequence(current_idx + 1, result_sequence, is_number_used, n):
                    return True

                # undo placement for backtracking
                result_sequence[current_idx + number_to_place] = 0

            # Undo current placement and mark number as unused
            result_sequence[current_idx] = 0
            is_number_used[number_to_place] = False

        return False

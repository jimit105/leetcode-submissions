# Approach 3: Bottom-Up Dynamic Programming

# n = len(str1), m = len(str2)
# Time: O(n * m * (n + m))
# Space: O(m * (n + m))

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)

        # Initialize the first row (when str1 is empty, the supersequence is str2's prefix)
        prev_row = [str2[:col] for col in range(str2_len + 1)]

        for row in range(1, str1_len + 1):
            # Initialize the first column (when str2 is empty, the supersequence is str1's prefix)
            curr_row = [str1[:row]] + [None for _ in range(str2_len)]

            for col in range(1, str2_len + 1):
                # If characters match, extend the supersequence from the diagonal value
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    # If characters do not match, choose the shorter supersequence 
                    # From previous row (exclude current str1 char)
                    pick_s1 = prev_row[col]
                    # From previous column (exclude current str2 char)
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (pick_s1 + str1[row - 1] if len(pick_s1) < len(pick_s2) 
                    else pick_s2 + str2[col - 1])

            # Move to next row
            prev_row = curr_row
        
        return prev_row[str2_len]

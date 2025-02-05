# Approach 2: Only Check Differences

# Time: O(n)
# Space: O(1)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        second_index_diff = 0
        num_diffs = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1

                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    first_index_diff = i
                else:
                    second_index_diff = i

        return (
            s1[first_index_diff] == s2[second_index_diff] and
            s1[second_index_diff] == s2[first_index_diff]
        )
        


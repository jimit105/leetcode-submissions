# Approach 3: Two Pointers / Greedy

# Time: O(S.T), S = length of source, T = length of target
# Space: O(1)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_chars = set(source)

        for char in target:
            if char not in source_chars:
                return -1

        m = len(source)
        source_iterator = 0

        count = 0

        for char in target:
            if source_iterator == 0:
                count += 1

            while source[source_iterator] != char:

                # Formula for incrementing while looping back to start.
                source_iterator = (source_iterator + 1) % m

                # If while finding, iterator reaches start of source again, increment count
                if source_iterator == 0:
                    count += 1

            # Loop will break when char is found in source. Thus, increment.
            # Don't increment count until it is not clear that target has
            # remaining characters.
            source_iterator = (source_iterator + 1) % m

        return count


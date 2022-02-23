# Approach 2 - Sorting by Keys

# Time: O(m * n logn), n = number of logs, m = max length of single log

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log):
            id_, rest = log.split(' ', maxsplit = 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        
        return sorted(logs, key = get_key)
            
        

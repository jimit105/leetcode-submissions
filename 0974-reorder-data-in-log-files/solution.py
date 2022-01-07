class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log):
            id_, rest = log.split(' ', maxsplit=1)
            
            # (0, rest, id_) for letter logs
            # (1, ) for digit logs
            return (0, rest, id_) if rest[0].isalpha() else (1, )
        
        return sorted(logs, key=get_key)

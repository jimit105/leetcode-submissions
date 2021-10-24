class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        result = ''
        for k, v in count.most_common():
            result += k*v
            
        return result
        

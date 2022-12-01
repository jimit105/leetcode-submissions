# Approach 3: Count Vowels (In Place + Function)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def count_vowels(s):
            ans = 0
            for c in s:
                if c in 'aieouAIEOU':
                    ans += 1
            return ans
        
        return count_vowels(s[:len(s) // 2]) == count_vowels(s[len(s) // 2 :])
        

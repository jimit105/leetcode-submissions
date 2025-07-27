class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbrev(word, i = 0):
            if (len(word) - i <= 3):
                return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = list(map(abbrev, words))
        prefix = [0] * N

        for i in range(N):
            while True:
                dupes = set()
                for j in range(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes:
                    break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        n = len(digits)

        for i in range(n):
            # Skip if first digit is 0
            if digits[i] == 0:
                continue

            for j in range(n):
                # Skip same index
                if i == j:
                    continue

                for k in range(n):
                    # Skip same index
                    if k == i or k == j:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if num % 2 == 0:
                        result.add(num)

        return sorted(list(result))

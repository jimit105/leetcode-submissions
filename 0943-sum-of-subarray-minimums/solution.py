# Approach: Monotonic Stack

# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/2118729/Very-detailed-stack-explanation-O(n)-or-Images-and-comments

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10 ** 9 + 7
        sums = 0
        arr.append(0)
        stack = [-1]
        
        for i2, num in enumerate(arr):
            # Maintain a monotonic increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                left = index - stack[-1]
                right = i2 - index
                sums += right * left * arr[index]
            stack.append(i2)
            
        return sums % M
        

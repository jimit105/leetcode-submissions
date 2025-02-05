# Approach 2: Better Stack Approach

# n = len(logs)
# Time: O(n)
# Space: O(n)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n

        # process first log entry
        s = logs[0].split(':')
        stack.append(int(s[0]))
        prev = int(s[2])

        i = 1
        while i < len(logs):
            s = logs[i].split(':')
            curr_time = int(s[2])

            if s[1] == 'start':
                if stack:
                    res[stack[-1]] += curr_time - prev
                stack.append(int(s[0]))
                prev = curr_time
            else:
                res[stack[-1]] += curr_time - prev + 1
                stack.pop()
                prev = curr_time + 1

            i += 1

        return res
        

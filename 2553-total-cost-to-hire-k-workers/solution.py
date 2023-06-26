# Approach 1: 2 Priority Queues

# Time: O(m + k * log m)
# Space: O(m)

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers stores the first k workers.
        # tail_workers stores at most last k workers without any workers from the first k workers.
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - candidates - 1

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heapq.heappop(head_workers)

                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1

            else:
                answer += heapq.heappop(tail_workers)

                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We will use max heap
        # heapq only supports min heap, so we convert all elements to negative
        for i, val in enumerate(stones):
            stones[i] *= -1
            
        heapq.heapify(stones)
        while len(stones) > 1:
            s = heapq.heappop(stones)
            t = heapq.heappop(stones)
            if s != t:
                heapq.heappush(stones, -abs(s-t))
        return abs(stones[0]) if stones else 0
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        # Reaching the top of the stair requires (len(cost) + 1) steps
        # The cost to reach the 0th and 1st step is 0
        minCost = [0] * (len(cost) + 1)
        
        for i in range(2, len(minCost)):
            minCost[i] = min(minCost[i-2] + cost[i-2], minCost[i-1] + cost[i-1])
            
        return minCost[-1]
        """

        # Dynamic programming backwards
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute force
        """
        maxProfit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i, len(prices)):
                buy = prices[i]
                sell = prices[j]
                maxProfit = max(maxProfit, sell - buy)
        return maxProfit
        """
        
        minBuy = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            if prices[minBuy] > prices[i]:
                minBuy = i
            else:
                maxSoFar = max(maxSoFar, prices[i] - prices[minBuy])
        return maxSoFar
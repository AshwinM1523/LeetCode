class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        bought = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= bought:
                bought = prices[i]
            else:
                total += prices[i] - bought
                bought = prices[i]
        
        return total
            
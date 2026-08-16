class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        buy = 100000

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            ans = max(ans, prices[i] - buy)
        
        return ans

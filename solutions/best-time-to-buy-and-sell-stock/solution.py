class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        l = 0
        r = l+1
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                best_profit = max(profit,best_profit)
            else:
                l = r
            r += 1
        return best_profit
            








class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minp = sys.maxsize

        for i in range(0, len(prices)):
            minp = min(minp, prices[i])
            profit_now = prices[i] - minp
            profit = max(profit, profit_now)

        return profit

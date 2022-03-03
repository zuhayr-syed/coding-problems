class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            profit = max(profit, price-buy)
            buy = min(buy, price)
        if profit < 0: profit = 0
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]

        for price in prices:
            if price < buyPrice:
                buyPrice = price
            profit = max(profit, price - buyPrice)

        return profit
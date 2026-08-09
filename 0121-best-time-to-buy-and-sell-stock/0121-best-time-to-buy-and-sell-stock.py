class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = prices[0]
        maxprofit=0
        for price in prices:
            if price < minprice:
                minprice=price
            profit = price - minprice
            if profit > maxprofit:
                maxprofit=profit
        return maxprofit

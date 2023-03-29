class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initializing profit to zero and minimum price to first price
        profit=0
        minp=prices[0]
        for i in range(len(prices)-1):
            # Checking if price is lesser than minimumprice
            # If so update minimum price
            if prices[i] < minp:
                minp=prices[i]
            # Checking if current prise - minimum price is greater then profit
            # If so update profit
            if (prices[i+1]-minp)>profit:
                profit=prices[i+1]-minp
        # Return profit
        return profit
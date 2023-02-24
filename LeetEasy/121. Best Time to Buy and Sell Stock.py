class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        minp=prices[0]
        for i in range(len(prices)-1):
            if prices[i] < minp:
                minp=prices[i]
            if (prices[i+1]-minp)>profit:
                profit=prices[i+1]-minp
        return profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = sys.maxint
        largestInterval = 0
        for i in range(len(prices)):
            if prices[i] <= smallest:
                smallest = prices[i]
            else:
                interval = prices[i] - smallest
                if interval > largestInterval:
                    largestInterval = interval
                    
        return largestInterval
                    
            

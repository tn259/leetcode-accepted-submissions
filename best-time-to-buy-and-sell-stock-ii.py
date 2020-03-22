class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      windowMin = 0
      windowMax = float("Inf")
      totalProfit = 0
      windowProfit = 0
      for p in prices:
        if p <= windowMax:
          windowMin = p
          windowMax = p
          totalProfit += windowProfit
          windowProfit = 0
        else:
          windowMax = p
          windowProfit = windowMax - windowMin
      
      totalProfit += windowProfit
      return totalProfit
        

class Solution:
    def climbStairsRec(self, n: int, table: dict) -> int:
      if n not in table:
        if n < 0:
           return 0
        if n == 0:
           return 1
        
        ways = 0
        
        ways += self.climbStairsRec(n-1, table)
        ways += self.climbStairsRec(n-2, table)
        
        table[n] = ways
      return table[n]
        
    #def tabulated(self, n: int) -> int:
      #table = [][]
      
      
      
    def climbStairs(self, n: int) -> int:
      table = {}
      return self.climbStairsRec(n, table)
        

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
        
    def tabulated(self, n: int) -> int:
      #table = [0] * 3
      #for j in range(3):
        #table[j] = [0] * (n+1)
      
      #for j in range(3):
        #for i in range(n+1):
          #if j==0 or i==0:
            #table[j][i] = 1
          #elif j==1:
            #table[j][i] = 1
          #else:
            #table[j][i] = table[j][i-1] + table[j][i-2]
      table = [1] * (n+1)
      for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
      return table[n]
            
      
      
    def climbStairs(self, n: int) -> int:
      #table = {}
      #return self.climbStairsRec(n, table)
      return self.tabulated(n)
        

class Solution:
    def next(self, n: int) -> int:
      res = 0
      while n > 0:
        res += (n%10)**2
        n = int(n / 10)
        
      return res
  
    def isHappy(self, n: int) -> bool:
        l = []
        while n != 1:
          l.append(n)
          n = self.next(n)

          if n in l:
            return False
          
        return True

class Solution:
    def countPrimes(self, n: int) -> int:
      # sieve of Eratosthenes

        if n <= 2:
          return 0
        
        table = {}
        for i in range(1, n):
          table[i] = True
        
        table[1] = False
        
        for i in range(1, n):
          if table[i] == True:
            for j in range(2*i, n, i):
              table[j] = False
        
        primes = []
        for k,v in table.items():
          if v == True:
            primes.append(k)
            
        return len(primes)

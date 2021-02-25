# Use heap based solution
# we populate with 1
# pop and increment count (when count == n return number popped)
# for primes multiply by popped num and push these guys in
# repeat but ensure no repeats occur by maintaining a set or lookup table
# heap store is log(m) where m is length of heap
# set is most likely implemented as tree so this lookup will be log 

# Space complexity O(n)
# Time complexity O(n * k log n)

import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ht = {1: True}
        q = [1]
        count = 0
        while q:
            prime_factor = heapq.heappop(q)
            count += 1
            if count == n:
                return prime_factor
            for prime in primes:
                new_prime_factor = prime * prime_factor
                if new_prime_factor not in ht:
                    ht[new_prime_factor] = True
                    heapq.heappush(q, new_prime_factor)

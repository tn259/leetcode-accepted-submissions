# at each book we consider its effect of putting it on a new shelf OR
# adding it on the same shelf as the previous books one be one backwards

# 0 1 2 3 4 5 6 7
# 0 1 3

#0 1 2 3 4 5 6 7
#0 1 4

# O(n^2) O(n)

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> 
        int:
        dp = [float('inf') for idx in range(len(books)+1)]
        dp[0] = 0
        for i in range(1, len(books)+1):
            width = shelf_width
            height = 0
            for j in reversed(range(1, i+1)):
                if width - books[j-1][0] >= 0:
                    height = max(height, books[j-1][1])
                    dp[i] = min(dp[i], dp[j-1] + height)
                    width -= books[j-1][0]
                else:
                    break
        return dp[-1]

################################################################
# Feels like a DP problem.
# we know that all squares n,e,s,w of water must only be of height 1 or 0.
# what we could try is to iterate the matrix
# at each water cell we go n, e, s, w until we encounter a non zero height 
    land cell/water cell/edge of grid
# we constrain the heights by the rules between height 0 and 

# matrix BFS at each water cell and calculate squares, minimise to rules i.e. 
    square is min(s,c+1) s is square, c is current square
# O(nm) S  + O(nm*(4^(n+m))) T
####################################################################

###############################
# Actual solution

class Solution:
    def inBounds(self, row, col, isWater) -> bool:
        height = len(isWater)
        width = len(isWater[0])
        return row < height and row >= 0 and col < width and col >= 0
                    
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        heights = [[-1]*len(isWater[0]) for _ in range(len(isWater))]
        # traverse through cells set water cells and insert
        q = deque()
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    heights[row][col] = 0
                    q.append([row, col])
        # bfs
        while len(q) > 0:
            point = q.popleft()
            row = point[0]
            col = point[1]
            candidateHeight = heights[row][col]+1
            for r, c in [[row-1, col], [row, col+1], [row+1, col], [row, col
                -1]]:
                # as this is bfs, the nearest water hole will always get to 
                    this position first
                # so once it has been inspected it is the minimum possible 
                    that it can be
                if self.inBounds(r, c, isWater) and heights[r][c] == -1:
                    heights[r][c] = candidateHeight
                    q.append([r,c])
        return heights

# DFS or BFS problem where we move a max of K moves and for each position 
    landed in the set of K moves we count
# on on board / on board + off board
# Easier to do DFS, we can move back to the same position we have already 
    visited
# Time Complexity - DFS O(8^K) ? at each move it can move in 8 dirs and it can 
    does it up to k times, if N is big enough this would be # the worst case
# Space complexity - O(K) for the recursion
# We could optimise this with DP since we could end up at the same square 
    again with the same remainning number of moves to go
# This would involve a N*N*K set of bools we'll optimise as an afterthought

class Solution:
    def isOffBoard(self, N: int, r: int, c: int) -> bool:
        if r < 0 or r > N-1:
            return True
        if c < 0 or c > N-1:
            return True
        return False
    
    def dfs(self, N: int, r: int, c: int, moves: int, K: int, table: list):
        if self.isOffBoard(N, r, c):
            return 0
        if moves == K:
            return 1      
        if table[r][c][moves] != None:
            return table[r][c][moves]
        localOnBoard = 0
        # right half
        localOnBoard += self.dfs(N, r-2, c+1, moves+1, K, table)
        localOnBoard += self.dfs(N, r-1, c+2, moves+1, K, table)
        localOnBoard += self.dfs(N, r+1, c+2, moves+1, K, table)
        localOnBoard += self.dfs(N, r+2, c+1, moves+1, K, table)
        # left half
        localOnBoard += self.dfs(N, r-2, c-1, moves+1, K, table)
        localOnBoard += self.dfs(N, r-1, c-2, moves+1, K, table)
        localOnBoard += self.dfs(N, r+1, c-2, moves+1, K, table)
        localOnBoard += self.dfs(N, r+2, c-1, moves+1, K, table)
        table[r][c][moves] = localOnBoard
        return table[r][c][moves]
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        table = [[[None for k in range(K)] for col in range(N)] for row in 
            range(N)]
        onBoard = self.dfs(N, r, c, 0, K, table)
        return float(onBoard) / (8 ** K)

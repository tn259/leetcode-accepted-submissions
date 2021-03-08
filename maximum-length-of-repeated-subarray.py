# Dynamic programming
# Tabular buildup T O(nm)
# space for initial solution O(nm) or O(min(n, m)) for space optimised 
    solution
# encode the longest length in first element
# encode length so far diagonaly in second element
# try optimisation of space, will improve To complexity of first matrix 
    creation

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        minList = A if len(A) > len(B) else B
        maxList = B if len(A) > len(B) else A
        
        oddList = [[0,0] for idx in range(len(minList)+1)]
        evenList = [[0,0] for idx in range(len(minList)+1)]
        
        for maxIdx in range(1, len(maxList)+1):
            isOdd = maxIdx % 2 != 0
            currentList = oddList if isOdd else evenList
            prevList = evenList if isOdd else oddList
            for minIdx in range(1, len(minList)+1):
                if minList[minIdx-1] != maxList[maxIdx-1]:
                    currentList[minIdx][0] = max(prevList[minIdx][0], 
                        currentList[minIdx-1][0])
                    currentList[minIdx][1] = 0
                else:
                    if maxIdx > 1 and minIdx > 1 and minList[minIdx-2] == 
                        maxList[maxIdx-2]:
                        currentList[minIdx][0] = max(prevList[minIdx-1][1]+1
                            , prevList[minIdx][0], currentList[minIdx-1][0])
                        currentList[minIdx][1] = prevList[minIdx-1][1]+1
                    else:
                        currentList[minIdx][0] = max(1, prevList[minIdx][0], 
                            currentList[minIdx-1][0])
                        currentList[minIdx][1] = 1
        return currentList[-1][0]
                    
        #table = [[[0,0]  for bIdx in range(len(B)+1)] for aIdx in range(len
            (A)+1)]
        #for aIdx in range(1, len(A)+1):
        #    for bIdx in range(1, len(B)+1):
        #        if A[aIdx-1] != B[bIdx-1]:
        #            table[aIdx][bIdx][0] = max(table[aIdx-1][bIdx][0], 
            table[aIdx][bIdx-1][0])
        #            table[aIdx][bIdx][1] = 0
        #        else:
        #            if aIdx > 1 and bIdx > 1 and A[aIdx-2] == B[bIdx-2]: # 
            continuos run?
        #                table[aIdx][bIdx][0] = max(table[aIdx-1][bIdx-1][1]
            +1, table[aIdx-1][bIdx][0], table[aIdx][bIdx-1][0])
        #                table[aIdx][bIdx][1] = table[aIdx-1][bIdx-1][1]+1
        #            else: # start of run?
        #                table[aIdx][bIdx][0] = max(1, table[aIdx
            -1][bIdx][0], table[aIdx][bIdx-1][0])
        #                table[aIdx][bIdx][1] = 1
        #return table[-1][-1][0]


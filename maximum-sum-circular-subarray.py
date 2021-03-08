

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # normal case
        runningMax = A[0]
        overallMax = runningMax
        for idx in range(1, len(A)):
            runningMax = max(A[idx], runningMax + A[idx])
            overallMax = max(runningMax, overallMax)
        
        runningMaxUp = [0 for n in A]
        runningMaxUp[0] = A[0]
        runningMaxDown = [0 for n in A]
        runningMaxDown[-1] = A[-1]
        # up
        runningMax = A[0]
        for idx in range(1, len(A)):
            runningMax += A[idx]
            runningMaxUp[idx] = max(runningMax, runningMaxUp[idx-1])
        # down
        runningMax = A[-1]
        for idx in reversed(range(len(A)-1)):
            runningMax += A[idx]
            runningMaxDown[idx] = max(runningMax, runningMaxDown[idx+1])
        # now all gaps
        for idx in range(1, len(A)-1):
            overallMax = max(overallMax, runningMaxUp[idx-1]
                +runningMaxDown[idx+1])
            
        return overallMax

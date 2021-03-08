class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costIdxToPassLength = {0:1, 1:7, 2:30}
        
        daysHT = {days[idx]: idx for idx in range(len(days))}
        
        matrix = [[float('inf') for day in range(max(days)+1)] for costIdx in 
            range(len(costs)+1)]
        for costIdx in range(len(costs)+1):
            matrix[costIdx][0] = 0
            
        for costIdx in range(1, len(costs)+1):
            for day in range(1, max(days)+1):
                # could be cheaper not to use type of ticket
                pricesToCompare = [matrix[costIdx-1][day]]
                if day not in daysHT:
                    # we don't have to buy a ticket to cover today
                    pricesToCompare += [matrix[costIdx][day-1]]
                for costTillNowIdx in range(1, costIdx+1):
                    # need to calculate cost of usig all types of ticket to 
                        cover this day that we have available
                    cost = costs[costTillNowIdx-1]
                    passLength = costIdxToPassLength[costTillNowIdx-1]
                    if day-passLength < 0:
                        pricesToCompare += [cost]
                    else:
                        pricesToCompare += [matrix[costIdx][day-passLength] + 
                            cost]
                matrix[costIdx][day] = min(pricesToCompare)
        
        return matrix[-1][-1]
                

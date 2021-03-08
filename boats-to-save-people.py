# greedy algorithm where we consume the most limit we can
# min possible value is len(people) / 2

# we could dump [weight, i] into an array and sort by weight
# then use two pointers by matching the smallest with the biggest
# if the biggest does not fit with the smallest at a given time then we have 
    to use one boat for the biggest and decrement biggest pointer
# this is O(n log n)
# O(n) space

# other method might involve a HT of weight to i, where we try to pair off 
    exact matches
# however this also would require some sort of sorted list to get the next 
    best match

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weightPersonList = [person for person in people]
        weightPersonList.sort()
        smallestIdx = 0
        largestIdx = len(weightPersonList)-1
        boatsRequired = 0
        while smallestIdx <= largestIdx:
            if weightPersonList[smallestIdx] + weightPersonList[largestIdx] <= 
                limit:
                smallestIdx += 1 # two can fit in this one
            boatsRequired += 1
            largestIdx -= 1
        return boatsRequired
        
        

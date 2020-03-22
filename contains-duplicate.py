class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      elementCounts = {}
      for n in nums:
        if n in elementCounts:
          return True
        else:
          elementCounts[n] = 1
          
      return False
        

class Solution:
    def robrec(self, nums: List[int], i: int, memoized: List[int]) -> int:
      if i >= len(nums):
        return 0
      
      if i == len(nums)-1 or i == len(nums)-2:
        return nums[i]
      
      if memoized[i] != -1:
        return memoized[i]
      
      greatest = 0
      for j in range(i+2, len(nums)):
        robbed = nums[i] + self.robrec(nums, j, memoized)
        if robbed > greatest:
          greatest = robbed
      
      memoized[i] = greatest
      return greatest
  
    def rob(self, nums: List[int]) -> int:
      memoized = [-1] * len(nums)
      r0 = self.robrec(nums, 0, memoized)
      r1 = self.robrec(nums, 1, memoized)
      if r0 > r1:
        return r0
      return r1
      



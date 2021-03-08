class Solution:
    def rob(self, nums: List[int]) -> int:
      
      if len(nums) == 0:
        return 0
      
      if len(nums) == 1:
        return nums[0]
    

      table = [0] * len(nums)
      
      table[len(nums)-1] = nums[len(nums)-1]
      table[len(nums)-2] = nums[len(nums)-2]
      
      for i in range(len(nums)-3,-1,-1):
        table[i] = table[i+2]+nums[i]
        if table[i+2]>table[i+1]:
          table[i+1] = table[i+2]
          
      if table[0] > table[1]:
        return table[0]
      
      return table[1]

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self, nums: List[int], l: int, r: int, n: TreeNode):
      if (l > r):
        return n
      
      if (r-l) % 2 == 0:
        mid = int(l + (r-l)/2)
      else:
        mid = int(l + (r-l)/2)+1
        
      n = TreeNode(nums[mid])
      n.left = self.rec(nums, l, mid-1, n.left)
      n.right = self.rec(nums, mid+1, r, n.right)
      return n
      
  
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      n = None
      n = self.rec(nums, 0, len(nums)-1, n)
      return n
        

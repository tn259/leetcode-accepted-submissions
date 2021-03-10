# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) T and S
# maintain the greatest value seen so far in the path
# good nodes are those that are greater than this value

class Solution:
    def goodNodesHelper(self, root: TreeNode, largest: int) -> int:
        node = root
        goodNodeCount = 1 if node.val >= largest else 0
        largest = max(largest, node.val)
        # recurse
        if node.left:
            goodNodeCount += self.goodNodesHelper(node.left, largest)
        if node.right:
            goodNodeCount += self.goodNodesHelper(node.right, largest)
        return goodNodeCount
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))

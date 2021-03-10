# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Solution 1 ###
# collect node at depth d-1 -> in order traversal
# for each do algorithm

# T Complexity of in order traversal is O(N) or O(sum(2**d-1) d=1 -> D)
# S complexity is the same as it is based on number of nodes at d-1

### Solution 2 ###
# same as Solution 1 except we insert as we go
# this way the only space complexity is the recursion

class Solution:
    #def collectParentNodes(self, root: TreeNode, d: int, nodes: 
        List[TreeNode]) -> None:
    #    pass
    
    def insertNewNodes(self, parentNode: TreeNode, v: int) -> None:
        originalLeft = parentNode.left
        originalRight = parentNode.right
        parentNode.left = TreeNode(val=v, left=originalLeft)
        parentNode.right = TreeNode(val=v, right=originalRight)
        
    def addOneRowRecursive(self, node: TreeNode, v: int, d: int, depth: int) 
        -> None:
        if depth == d-1:
            self.insertNewNodes(node, v)
        else:
            if node.left:
                self.addOneRowRecursive(node.left, v, d, depth+1)
            if node.right:
                self.addOneRowRecursive(node.right, v, d, depth+1)
    
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newRoot = TreeNode(val=v, left=root)
            return newRoot
        depth = 1
        self.addOneRowRecursive(root, v, d, depth)
        return root

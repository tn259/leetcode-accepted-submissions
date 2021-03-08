# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) T and S
# maintain the greatest value seen so far in the path
# good nodes are those that are greater than this value

#class Solution:
#    def goodNodesHelper(self, root: TreeNode, largest: int) -> int:
#        node = root
#        goodNodeCount = 1 if node.val >= largest else 0
#        largest = max(largest, node.val)
#        # recurse
#        if node.left:
#            goodNodeCount += self.goodNodesHelper(node.left, largest)
#        if node.right:
#            goodNodeCount += self.goodNodesHelper(node.right, largest)
#        return goodNodeCount
    
#    def goodNodes(self, root: TreeNode) -> int:
#        return self.goodNodesHelper(root, float('-inf'))

# iterative based approach:
# Use a stack of nodes and a stack of largest values as we traverse up/down 
    the tree
# switch on a goLeft/right bool
# when going up we ask if we are a left child or right child
# if a left child we go down right
# if a right child we continue going up

class Solution:
    def isGoodNode(self, node: TreeNode, largest_stack: list):
        return node.val >= largest_stack[-1]
    
    def goodNodeHelper(self, node: TreeNode, largest_stack: list):
        return 1 if self.isGoodNode(node, largest_stack) else 0
    
    def goodNodes(self, root: TreeNode) -> int:
        node = root
        node_stack = [node]
        largest_stack = [float('-inf')]
        go_left = True
        good_nodes = 0
        while node_stack:
            node = node_stack[-1]
            if go_left:
                # do logic for working out 
                good_nodes += self.goodNodeHelper(node, largest_stack)
                if self.isGoodNode(node, largest_stack):
                    largest_stack += [node.val]
                else:
                    largest_stack += [largest_stack[-1]]
                # now go left
                if node.left:
                    node_stack += [node.left]
                else:
                    go_left = False
            else:
                if node.right:
                    node_stack += [node.right]
                    go_left = True
                else:
                    # no nodes left or right
                    # at the end 
                    node_stack.pop(-1)
                    largest_stack.pop(-1)
                    while node_stack:
                        parent = node_stack[-1]
                        if parent.right == node:
                            node = parent
                            node_stack.pop(-1)
                            largest_stack.pop(-1)
                        else:
                            break
        return good_nodes
        
                            
                            
                        
                        

                    


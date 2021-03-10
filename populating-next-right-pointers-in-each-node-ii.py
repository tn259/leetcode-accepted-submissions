"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None
        , next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# O(1) space

class Solution:
    def getNextLevelHead(self, node: 'Node'):
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None
    
    def connect(self, root: 'Node') -> 'Node':
        levelHead = Node(-1, next=root)
        while levelHead.next != None:
            node = levelHead.next
            needle = Node(-1)
            # thread through needle
            while node:
                if node.left:
                    needle.next = node.left
                    needle = needle.next
                if node.right:
                    needle.next = node.right
                    needle = needle.next
                node = node.next
            # now go to the next level
            levelHead.next = self.getNextLevelHead(levelHead.next)
        return root
            
                        
